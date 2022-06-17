from flask import Blueprint, render_template


students = Blueprint('students', __name__)

@students.route('/students')
def index():
    
    return render_template('students/students.html')
