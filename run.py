#creates the FLASK_APP environment variable which starts the flask server. use export FLASK_APP=run.py and flask run in the command line
import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
