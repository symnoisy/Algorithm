from flask_restplus import fields
from flaskencodeparser import FlaskModel

class BiggestNumberModel(object):
    def __init__(self, ns):

        primodel = {
            'numbers': fields.String(default='all', required=True, example="[6,10,2]"),
            'result': fields.String(default='all', required=True, example='6210')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})


class MarthonModel(object):
    def __init__(self, ns):

        primodel = {
            'participant': fields.String(default='all', required=True, example="['leo','kiki','eden']"),
            'completion': fields.String(default='all', required=True, example="['kiki','eden']"),
            'result': fields.String(default='all', required=True, example='eden')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})


class PhoneBookModel(object):
    def __init__(self, ns):

        primodel = {
            'phoneBook': fields.String(default='all', required=True, example="[119,97674223,1195524421]"),
            'result': fields.String(default='all', required=True, example='eden')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})