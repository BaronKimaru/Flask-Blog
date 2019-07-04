import os

SECRET_KEY = "JHCUDGIDJHGUICJHTY%^#&*(OIEJDHBGYT^&*IUBHDGVEFYT^#*&UI"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://", os.environ.get('DBWORKUSER'), ":", os.environ.get('DBWORKPASSWORD'), "@", os.environ.get('DBWORKHOST') , "/", os.environ.get('DBWORKDATABASE')
