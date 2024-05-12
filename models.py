from dbapp import db


class Person (db.Model):
    __tablename__='people'
    pid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text,nullable=True)
    age=db.Column(db.Integer)
    job=db.Column(db.Text)

    def __repr__(self) :
        return f'Person with name {self.name} and age {self.age}'