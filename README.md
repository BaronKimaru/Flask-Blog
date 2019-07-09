# FlaskStructure

### This is a Basic shell of your flask app, i.e, How your app should be organized.
This is a case where you may choose to store those configurations you wouldnt want to push to Version control.\
You may choose to store them in the Instance/config folder but this is genrally frowned upon.\
Ideally, it's better to have your configurations in a '.env' and then access them via the dotenv module 

#NB, In this, Ive used the structure of:
```
main_project:
            app:
                __init__.py
                views.py
                models.py
                templates
                static
            instance:
                config.py (houses all the secret files and passwords you wish to keep from version control)
            config.py     (has all the dev, testing, staging & production configs)
            run.py
            requirements.txt
venv
```

## INSTALL
###### clone the repository
git clone https://github.com/BaronKimaru/FlaskStructure.git<br />
\
cd flaskstructure

Create a virtualenv and activate it:

python3 -m venv venv
. venv/bin/activate

Run
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
Or on Windows cmd:

set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
Open http://127.0.0.1:5000 in a browser.
