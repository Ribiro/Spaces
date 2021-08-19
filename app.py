from flask import Flask, Blueprint
from flask_restx import Api
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)

# swagger route kind of thing
blueprint = Blueprint('Space and Uppercase', __name__, url_prefix='/api/v1')

ma = Marshmallow(app)
CORS(app)

api = Api(blueprint, title='Spaces and Uppercase', description='This is a Spaces and Uppercase API', version='1.0', author='Dennis',
          contact_email='ribirodenis05@gmail.com', doc='/doc')
app.register_blueprint(blueprint)


from controller.InputController import ns_input

api.add_namespace(ns_input)