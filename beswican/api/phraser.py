from flask import Flask
from flask_restful import Resource, Api
from flask import Blueprint
import json

from beswican.core import phrase_generator

api_blueprint = Blueprint('api_blueprint', __name__)
phrase_api = Api(api_blueprint)


@api_blueprint.route('/phrase', methods=['GET'])
def get_phrase():
    """
        Return a generated buzz phrase.

        :return:
    """
    response_json = json.dumps({'phrase': phrase_generator.generate_phrase()})
    return response_json
