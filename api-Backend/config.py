import os
from dotenv import load_dotenv
from decouple import config as config_env


basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()
class Config:
    SECRET_KEY = config_env('SECRET_KEY')#os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
    #     or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # 'mssql+pymssql://user:pass@server:port/?charset=utf8'
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://'+\
                    config_env('DB_USER') + ':' + \
                    config_env('DB_PASS') +'@' + \
                    config_env('DB_SERVER') + ':' + \
                    config_env('DB_PORT') + '/?charset=utf8'


    SQLALCHEMY_TRACK_MODIFICATIONS = False