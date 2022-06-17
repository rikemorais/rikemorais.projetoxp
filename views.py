from sys import prefix
from flask import render_template, request, redirect, url_for
from app import db, app
from models import Students


# Main
@app.route('/')
def index():
    students = Students.query.all()
    return render_template('students/students.html', students = students)


# Create Student
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
    