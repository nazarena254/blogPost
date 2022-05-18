import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
   
    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config): #this configuration is needed during heroku deployment, also change it to heroku DATABASE_URL Config Var 
    SQLALCHEMY_DATABASE_URI = 'postgresql://wvfuhmjfoxmwet:598506b7a82c560f8c14bfd651706c265441486efb9a05f77aaac5859a0bcbf5@ec2-3-229-11-55.compute-1.amazonaws.com:5432/db33vndr44ue9e'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://nancyngunjiri1:nazarenah123@localhost/blog"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://nancyngunjiri1:nazarenah123@localhost/blog"
    DEBUG=True
    
config_options = {'development':DevConfig, 'production':ProdConfig, 'test':TestConfig}
    
