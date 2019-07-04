import os

from app import create_app

config_name = os.environ.get('FLASK_CONFIG')
print("config name: ", config_name)

app = create_app(config_name)

if __name__ == '__main__':
	app.run()