import os
import threading
import secrets

from rest import algorithm
from config_variable import logger
from flask_restplus.resource import Resource
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from service_algorithm import AlgorithmService
from time import gmtime, strftime

@algorithm.route('/', methods=['GET'])
class ReturnAllURL(Resource):
    '''
    존재하는 모든 api 접근 url 반환하는 서비스
    '''
    @algorithm.doc(description='존재하는 모든 api의 접근 url을 반환합니다.')
    def get(self):
        result_allurl = {
            'all_services': "/algorithm",
        }
        return result_allurl

@algorithm.route('/algorithm', methods=['GET'])
class ReturnAllChallenges(Resource):
    @algorithm.doc(description='algorithm service')

    def get(self):
        rnnservice = AlgorithmService()
        result_rnnservice = rnnservice.test()
        return result_rnnservice