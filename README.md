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
            config.py(has all the dev, production configs)
            run.py
            requirements.txt
venv
```
