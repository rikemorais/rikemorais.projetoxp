from flask import Flask
from api.routes import api
from apps.students.routes import students


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(students)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)