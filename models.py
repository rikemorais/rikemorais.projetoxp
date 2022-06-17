from app import db

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