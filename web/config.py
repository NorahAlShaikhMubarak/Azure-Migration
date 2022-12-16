import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdb0.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="azureuser@techconfdb0" #TODO: Update value
    POSTGRES_PW="Nourah98fplij"   #TODO: Update value
    POSTGRES_DB="techconfdatabase"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://project3servicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=qcA8oxaIT79UxKXSzQuMPpTwvQjZjzjoWlfzhXxQ8hA=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'norahhamad98@outlook.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False