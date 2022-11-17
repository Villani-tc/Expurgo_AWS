import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime

ACCESS_KEY = ''
SECRET_KEY = ''
buck = ''

session = boto3.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name="sa-east-1")

s3s = session.resource("s3")
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

objects = s3.list_objects(Bucket=buck, MaxKeys=123)

list_ob = []
to_purge = []
today = str(datetime.now())[:-4]
today = today.replace('.', ':')
today = datetime.today().strptime(today, '%Y-%m-%d %H:%M:%S:%f')

for obs in objects["Contents"]:
    dat = str(obs["LastModified"])
    dat = dat.replace('+', ':')
    dat = dat[:-3]
    list_ob.append(obs['Key'] + '$' + str(dat))
for obj in list_ob:
    obj = obj.split('$')
    name_obj = obj[0]
    data = obj[1]
    data = datetime.strptime(data, '%Y-%m-%d %H:%M:%S:%f')
    x = 40 #[INT] Quantidade de dias para expurgar o arquivo.
    diff = (today - data)
    '''if diff.days < x:                                           #Linha de código opcional para mostrar quais arquivos seriam expurgados e quais não.
        print('Sem Expurgo ' + str(name_obj))                   
    else:
        to_purge.append(name_obj)
        print('Expurgo para ' + str(name_obj))'''
    to_purge.append(name_obj)
    print('Expurgo para ' + str(name_obj))

for key in to_purge:
    s3s.Object(buck, key).delete()
    print('Arquivo ' + str(key) + ' Deletado')
