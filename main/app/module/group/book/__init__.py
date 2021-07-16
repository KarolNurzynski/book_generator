from flask import Blueprint
book_blueprint = Blueprint("book", __name__, template_folder="templates")

from . import bookView
