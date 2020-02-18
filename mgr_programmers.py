from flask_restplus import fields
from flaskencodeparser import FlaskModel

class MarthonModel(object):
    def __init__(self, ns):

        primodel = {
            'participant': fields.String(default='all', required=True, example="['leo','kiki','eden']"),
            'completion': fields.String(default='all', required=True, example="['kiki','eden']"),
            'result': fields.String(default='all', required=True, example='eden')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})

