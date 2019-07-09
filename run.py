import os

from project import create_app

config_name = os.environ.get('FLASK_CONFIG')
print("config name: ", config_name)

app = create_app(config_name)


# You dont need to include the below if you have FLASK_APP in your env variables
# if __name__ == '__main__':
# 	app.run()
