from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from apps.students.routes import students

# Flask App
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    # Blueprints
    app.register_blueprint(api)
    app.register_blueprint(students)   
    return app


app = create_app()
db = SQLAlchemy(app)


from apps.students.views import *


if __name__ == '__main__':    
    app.run(debug=True)