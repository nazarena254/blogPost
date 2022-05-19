from app import app
from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Post, Comment, PostLike


#change from 'development to production' when deploying to heroku
#Creating app instance
app=create_app('production')

manager=Manager(app)
manager.add_command('server',Server)

migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Comment=Comment, PostLike=PostLike)
    
@manager.command
def test():
    import unittest
    test=unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity = 2).run(test)
    
if __name__=='__main__':
    app.config['SECRET_KEY'] = 'renahwambo' #add secret key configaration
    manager.run() 
    
