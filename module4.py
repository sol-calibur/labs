from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#init
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

#book class
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __init__(self, book_name, author, publisher):
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

#create book
@app.route('/book', methods=['POST'])
def add_book():
    book_name = request.form['book_name']
    author = request.form['author']
    publisher = request.form['publisher']

    new_book = Book(book_name, author, publisher)
    db.session.add(new_book)
    db.session.commit()

    return jsonify({
        'id': new_book.id,
        'book_name': new_book.book_name,
        'author': new_book.author,
        'publisher': new_book.publisher
    })

#retrieve every book
@app.route('/books', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    result = [
        {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        } for book in all_books
    ]
    return jsonify(result)

#retrieve book by id
@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify({
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    })

#update book by id
@app.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    book_name = request.form['book_name']
    author = request.form['author']
    publisher = request.form['publisher']

    book.book_name = book_name
    book.author = author
    book.publisher = publisher

    db.session.commit()
    return jsonify({
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    })

#delete book by id
@app.route('/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

#run app
if __name__ == '__main__':
    app.run(debug=True)