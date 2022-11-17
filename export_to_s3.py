import boto3
from botocore.exceptions import NoCredentialsError
import glob


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

s3 = boto3.client('s3')

ACCESS_KEY = ''
SECRET_KEY = ''
buck = ''
direct_data = 'C:..' #Diretório com os arquivos que vão subir para o AWS
direct_domain = 'C:..' #Diretório com os arquivos que vão subir para o AWS
data = glob.glob(str(direct_data) + '/*.zip', recursive=True) #Tipo de arquivo que vai subir (/*.zip, /*.csv ,/.txt etc.)
domain = glob.glob(str(direct_domain) + '/*.zip', recursive=True)#Tipo de arquivo que vai subir (/*.zip, /*.csv ,/.txt etc.)
for file in domain:
    upload_to_aws(file, buck, 'Nome do arquivo')
for file in data:
    upload_to_aws(file, buck, 'Nome do arquivo')

