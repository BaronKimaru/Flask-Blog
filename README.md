# Flask Blog App

#### Ideally, this is an small example of a Blog app, showcasing how your app should be organized.
This is a case where you may choose to store those configurations you wouldnt want to push to Version control.\
You may choose to store them in the Instance/config folder but this is genrally frowned upon.\
Generally, it's better to have your configurations in a '.env' and then access them via the dotenv module 

#NB, In this, Ive used the structure of:
```
main_project:
.       project:
.               __init__.py
.               views.py
.                models.py
.               templates:- base.html
.               static
.               home:
.                   __init__.py
.                   routes.py
.                   templates/home:- index.html,about.html, contact.html
.                   static:
.                         css: styles.css
.                         js: main.js
.               users:
.                   __init__.py
.                   routes.py
.                   templates/users:- login.html, profile.html, register.html
.                   static:
.                         css: styles.css
.                         js: main.js
.               posts:
.                   __init__.py
.                   routes.py
.                   templates/posts:- posts.html, post.html, addpost.html, editpost.html, deletepost.html
.                   static:
.                         css: styles.css
.                         js: main.js
.               tests:
.                     functional: model
.                     auth: views
.         instance:
.                 config.py (houses all the secret files and passwords you wish to keep from version control)
.         config.py       (has all the dev, testing, staging & production configs)
.         run.py
.         requirements.txt
venv
```

## INSTALL/ Clone the Repository  
git clone https://github.com/BaronKimaru/FlaskBlog.git  
  
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
