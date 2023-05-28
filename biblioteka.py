# biblioteka.py

from app import app, db
from app.models import Book, Informations

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "Informations": Informations
   }