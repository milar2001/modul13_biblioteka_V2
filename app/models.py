# app/models.py
from datetime import datetime
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    book_title = db.Column(db.String(100), index=True, unique=True)
    author = db.Column(db.String(200), index=True)
    information = db.relationship("Informations", backref="rented", lazy="dynamic")

    def __str__(self):
        return f"<Name {self.book_title}>"

class Informations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower_name = db.Column(db.String(100), index=True)
    borrower_last_name = db.Column(db.String(100), index=True)
    borrowed_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_rented = db.Column(db.Boolean, index=True, default=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Informations {self.id} {self.borrower_name} {self.borrower_last_name}>"