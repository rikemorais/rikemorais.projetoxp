from flask import Blueprint

students = Blueprint('students', __name__)

@students.route('/')
def index():
    return '<h1>Students</h1>'
