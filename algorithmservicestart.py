from flask import Flask
from flask_cors.extension import CORS

from rest import blueprint
from config_variable import bind_addr, bind_port, logger
from rest_algorithm import *

app = Flask(__name__)
CORS(app)
app.register_blueprint(blueprint)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


class Service():

    def restInit(self):
        '''
        flask-restplus 서비스 시작
        '''

        logger.info('Rest Service start. url=http://' + bind_addr + ':' + str(bind_port) + '/swagger')
        app.run(host=bind_addr, port=bind_port, debug=False)

    def start(self):
        logger.info('RNN Service start.')
        self.restInit()


if __name__ == '__main__':
    global service
    service = Service()
    service.start()
