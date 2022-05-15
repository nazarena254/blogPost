import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://nancyngunjiri1:nazarenah123@localhost/blog"
   
    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config): #this configuration is needed during heroku deployment, also change it to heroku DATABASE_URL Config Var 
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://nancyngunjiri1:nazarenah123@localhost/blog"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://nancyngunjiri1:nazarenah123@localhost/blog"
    DEBUG=True
    
config_options = {'development':DevConfig, 'production':ProdConfig, 'test':TestConfig}
    
