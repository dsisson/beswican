from flask import render_template
from flask import Blueprint
from beswican.core import phrase_generator

web = Blueprint('web', __name__, template_folder='templates', static_url_path='./static',
                static_folder='static')


@web.route('/')
@web.route('index.html')
def index():
    phrase = phrase_generator.generate_phrase()
    return render_template('index.html', phrase=phrase)

