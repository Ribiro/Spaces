from flask_restx import Namespace, fields


class Input:
    ns_input = Namespace('Input', description='Input related operations')
    input = ns_input.model('inputModel', {
        'input': fields.String(required=True, description='input to process'),
    })
