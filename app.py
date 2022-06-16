from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from apps.students.routes import students

# Flask App
def create_app():
    app = Flask(__name__)
    # Blueprints
    app.register_blueprint(api)
    app.register_blueprint(students)   
    return app

app = create_app()

# Database Connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'projetoxp'
    )

db = SQLAlchemy(app)


# Database Models
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone = db.Column(db.String(15), nullable = False)
    
    def __repr__(self):
        return '<id %r>' % self.id


class Users(db.Model):
    name = db.Column(db.String(20), nullable = False)
    nickname = db.Column(db.String(10), primary_key=True)
    key = db.Column(db.String(100), nullable = False)
    
    def __init__(self, name, nickname, key):
        self.name = name
        self.nickname = nickname
        self.key = key
    
    def __repr__(self):
        return '<Name %r>' % self.name
    

@app.route('/')
def index():
    students = Students.query.all()
    return render_template('students/students.html', students = students)


@app.route('/create', methods=['POST',])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        data = Students(name=name, email=email, phone=phone)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('index'))


if __name__ == '__main__':    
    app.run(debug=True)