from flask_restx import Resource
from util.InputUtil import Input

ns_input = Input.ns_input
input_model = Input.input

from service.InputService import *


@ns_input.route('')
class InputList(Resource):
    @ns_input.expect(input_model)
    def post(self):
        """Use this endpoint to process your input"""
        input = ns_input.payload
        return process_input(input)
