from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return self.name

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    borrowed = db.Column(db.Boolean, default=False)
    returned = db.Column(db.Boolean, default=False)
    borrow_details = db.relationship('BorrowDetails', backref='book', uselist=False)

class BorrowDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrower_name = db.Column(db.String(100), nullable=False)
    borrowed_date = db.Column(db.DateTime, nullable=False)
    returned_date = db.Column(db.DateTime)
