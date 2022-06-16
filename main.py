from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from apps.students.routes import students


def create_app():
    app = Flask(__name__)

    # Blueprints
    app.register_blueprint(api)
    app.register_blueprint(students)
           
    return app

# App Instance
app = create_app()

# Database Connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"{'mysql+mysqlconnector'}://{'root'}:{'admin'}@{'localhost'}/{'projetoxp'}"
db = SQLAlchemy(app)

# Database Tables
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone = db.Column(db.String(15), nullable = False)
    
    def __repr__(self):
        return '<Name %r>' % self.name


class Users(db.Model):
    name = db.Column(db.String(20), nullable = False)
    nickname = db.Column(db.String(10), primary_key=True)
    key = db.Column(db.String(100), nullable = False)
    
    def __repr__(self):
        return '<Name %r>' % self.name


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)