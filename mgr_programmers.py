from flask_restplus import fields
from flaskencodeparser import FlaskModel

#Hash (3/4)
class MarthonModel(object):
    def __init__(self, ns):

        primodel = {
            'participant': fields.String(default='all', required=True, example="['leo','kiki','eden']"),
            'completion': fields.String(default='all', required=True, example="['kiki','eden']"),
            'result': fields.String(default='all', required=True, example='leo')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})


class PhoneBookModel(object):
    def __init__(self, ns):

        primodel = {
            'phoneBook': fields.String(default='all', required=True, example="[119,97674223,1195524421]"),
            'result': fields.String(default='all', required=True, example='False')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})


class CamouflageModel(object):
    def __init__(self, ns):

        primodel = {
            'clothes': fields.String(default='all', required=True, example='[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]'),
            'result': fields.String(default='all', required=True, example='5')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})


#Stack/Queue (2/6)
class TopModel(object):
    def __init__(self, ns):
        primodel = {
            'heights': fields.String(default='all', required=True, example="[6,9,5,7,4]"),
            'result': fields.String(default='all', required=True, example='[0,0,2,2,4]')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})

class FunctionDevelopModel(object):
    def __init__(self, ns):
        primodel = {
            'progresses': fields.String(default='all', required=True, example='[93,30,55]'),
            'speeds': fields.String(default='all', required=True, example='[1,30,5]'),
            'result': fields.String(default='all', required=True, example='[2,1]')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})


#Heap (0/4)
#Sorting (3/3)
class NumberKModel(object):
    def __init__(self, ns):

        primodel = {
            'array': fields.String(default='all', required=True, example="[1,5,2,6,3,7,4]"),
            'commands': fields.String(default='all', required=True, example="[[2,5,3],[4,4,1],[1,7,3]]"),
            'result': fields.String(default='all', required=True, example='[5,6,3]')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})

class BiggestNumberModel(object):
    def __init__(self, ns):

        primodel = {
            'numbers': fields.String(default='all', required=True, example="[6,10,2]"),
            'result': fields.String(default='all', required=True, example='6210')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})

class HIndexModel(object):
    def __init__(self, ns):

        primodel = {
            'citations': fields.String(default='all', required=True, example="[3,0,6,1,5]"),
            'result': fields.String(default='all', required=True, example='3')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})

#AbsoluteSearch (1/4)
class MockTestModel(object):
    def __init__(self, ns):

        primodel = {
            'answers': fields.String(default='all', required=True, example="[1,2,3,4,5]"),
            'result': fields.String(default='all', required=True, example='[1]')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})


#Greedy (0/7)
#DynamicProgramming (0/7)
#DFS/BFS_Search (1/4)
class TargetNumberModel(object):
    def __init__(self, ns):

        primodel = {
            'numbers': fields.String(default='all', required=True, example="[1,1,1,1,1]"),
            'target': fields.String(default='all', required=True, example="3"),
            'result': fields.String(default='all', required=True, example='5')
        }

        self.get = FlaskModel(self, ns, 'get', {**primodel})

#BinarySearch (0/3)
#Graph (0/4)