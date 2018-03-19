from flask import Flask
from flask import Blueprint
from beswican.core import phrase_generator
#from beswican.runserver import app

website_bp = Blueprint('website', __name__)


@website_bp.route("/")
def generate_phrase():
    page = '<html><body><h1>'
    page += phrase_generator.generate_phrase()
    page += '</h1></body></html>'
    return page

