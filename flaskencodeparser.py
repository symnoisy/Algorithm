import flask_restplus

class FlaskModel():
    '''
    swagger에 표시되는 model 생성
    '''

    _model = None
    _schema = None

    def __init__(self, owner, ns, name, model, mask=None, as_list=False, **kwargs):

        if model is None:
            raise ValueError('model is None.')

        if isinstance(model, dict):
            modelName = owner.__class__.__name__ + '-' + name
            self._model = ns.model(modelName, model, mask, *kwargs)

            prop = {}
            for key, value in self._model.items():
                if isinstance(value, flask_restplus.fields.Nested):
                    prop[key] = value.model._schema
                else:
                    prop[key] = value.__schema__

            self._schema = self._model._schema
            self._schema['properties'] = prop
        else:
            self._schema = model.__schema__

        if as_list:
            self._schema = {
                'type': 'array',
                'items': self._schema
            }

    @property
    def model(self):
        return getattr(self, '_model')

    @property
    def schema(self):
        return getattr(self, '_schema')