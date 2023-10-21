import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')

    # MySQL Database Configuration
    DB_USERNAME = os.getenv('DB_USERNAME', 'shsyqtmt_datalock')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'tItsurdA1W6Yu9kTzX')  # Cambia 'password' por tu contraseña real
    DB_HOST = os.getenv('DB_HOST', 'muud.cloud')
    DB_PORT = os.getenv('DB_PORT', '3306')
    DB_NAME = os.getenv('DB_NAME', 'shsyqtmt_datalock')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')    
    
    SOCIAL_AUTH_GITHUB = False

    GITHUB_ID = os.getenv('GITHUB_ID')
    GITHUB_SECRET = os.getenv('GITHUB_SECRET')

    # Enable/Disable Github Social Login    
    if GITHUB_ID and GITHUB_SECRET:
         SOCIAL_AUTH_GITHUB = True

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
