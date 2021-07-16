from flask import render_template, request, flash, redirect, url_for
from . import book_blueprint
from .bookForm import BookForm
from .bookModel import Book
from app import db

@book_blueprint.route("/book", methods=["GET", "POST"])
def createBook():
    form = BookForm(request.form)
    books = Book.query.all()
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)
        db.session.add(book)
        db.session.commit()
        flash("Added Book Successfully")
        return redirect(url_for("book.createBook"))
    return render_template("book.html", title="Book", form=form, books=books)

@book_blueprint.route("/updateBook/<int:book_id>", methods=["GET", "POST"])
def updateBook(book_id):
    book = Book.query.get(book_id)
    form = BookForm(request.form, obj=book)
    if form.validate_on_submit():
        form.populate_obj(book)
        db.session.commit()
        flash("Updated Book Successfully")
        return redirect(url_for("book.createBook"))
    return render_template("book.html", title="Book", form=form, books=Book.query.all())

@book_blueprint.route("/deleteBook/<int:book_id>", methods=["GET", "POST"])
def deleteBook(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("book.createBook"))
