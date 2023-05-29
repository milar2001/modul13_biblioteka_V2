# app/routes.py
from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import Book, Author, BorrowDetails
from app.forms import BookForm
import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    books = Book.query.all()
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        borrower_name = request.form.get('borrower_name')

        book = Book.query.get(book_id)
        if book:
            if not book.borrowed:
                borrow_details = BorrowDetails(book_id=book_id, borrower_name=borrower_name, borrowed_date=datetime.datetime.now())
                db.session.add(borrow_details)
                book.borrowed = True
                db.session.commit()

    return render_template('index.html', books=books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        author = Author.query.filter_by(name=form.author.data).first()
        if not author:
            author = Author(name=form.author.data)
            db.session.add(author)
            db.session.commit()

        book = Book(title=form.book_title.data, author=author)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)

@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get(book_id)
    return render_template('book_details.html', book=book)

@app.route('/book/<int:book_id>/return', methods=['POST'])
def return_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.borrowed:
        book.borrowed = False
        if book.borrow_details:
            borrower_name = book.borrow_details.borrower_name
            db.session.delete(book.borrow_details)
            flash(f'Książka została zwrócona przez {borrower_name} i dane wypożyczającego zostały usunięte.', 'success')
        else:
            flash('Książka została zwrócona.', 'success')
        db.session.commit()
    else:
        flash('Książka nie jest wypożyczona.', 'danger')
    return redirect(url_for('book_details', book_id=book_id))