   COMMANDS TO GET STARTED
* Run `sudo apt-get update`,`sudo apt-get install python3.6` in terminal to install python.
* Run `python3.9 -m venv --without-pip virtual` in terminal to install virtual environment.
* Run `source virtual/bin/activate` to activate and `.../deactivate` to deactivate virtual env.
* Run `curl https://bootstrap.pypa.io/get-pip.py | python` to install pip in virtual env.
* Run `pip install <packagename>` to install other dependencies.
* Run `pip install -r requirements.txt` to install all dependencies in requirements.txt file .

  INSTALL POSTGRESQL BD
*  sudo apt-get update
*  sudo apt-get install postgresql postgresql-contrib libpq-dev

   START SERVER
* Run `python3.9 manage.py server` to start server.
* Alternatively `chmod a+x start.sh` , `./start.sh`
   
   DEPLOYMENT TO HEROKU
* To deploy on heroku, you will need to install/do the following:
   - outline dependencies `pip freeze`  
   - add dependencies in requirements.txt file `pip freeze > requirements.txt`
   - heroku cli `npm install -g heroku`
   - gunicorn  `python3.9 -m pip install gunicorn`
   - in config.py: add the following cofiguration.
     class ProdConfig(Config) 
         SQLALCHEMY_DATABASE_URI= heroku DATABASE URL Config Var
   - in manage.py file change app from development to production
         app=create_app('production') 
   - `heroku login` to login in heroku using cli
   - `heroku create <appname> ` to create appname
   - `heroku config:set SECRET_KEY=<surecretkey>` and MAIL_USERNAME, MAIL_PASSWORD...etc 
   - `heroku addons:create heroku-postgresql`  to setup postgres in heroku
   - `git add .` `git commit -m "message" ` & `git push heroku master`       
   - `heroku run python3 manage.py db upgrade` to update heroku server.

   MIGRATIONS 
* To enable migrations:
   - Initialize migration `python3.9 manage.py db init`
   - Create migration `python3.9 manage.py db migrate -m "migration message"`  
   - Upgrade migration `python3.9 manage.py db upgrade` 