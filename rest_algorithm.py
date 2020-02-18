import os
import threading
import secrets

from marshmallow import fields
from rest import programmers
from mgr_programmers import MarthonModel
from config_variable import logger
from flask_restplus.resource import Resource
from webargs.flaskparser import use_kwargs
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from service_programmers import HashAlgorithm
from time import gmtime, strftime

marathonModel = MarthonModel(programmers)

@programmers.route('/', methods=['GET'])
class ReturnAllURL(Resource):
    '''
    존재하는 모든 api 접근 url 반환하는 서비스
    '''
    @programmers.doc(description='존재하는 모든 api의 접근 url을 반환합니다.')
    def get(self):
        result_allurl = {
            'all_services': "/algorithm",
        }
        return result_allurl

@programmers.route('/hash/marathon', methods=['GET'])
class ReturnAllChallenges(Resource):
    @programmers.doc(description='완주하지 못한 선수 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3')

    @programmers.param('participant', '마라톤 참가자', _in = 'query', type = str, required = True, default = "['leo','kiki','eden']")
    @programmers.param('completion', '마라톤 완주자', _in='query', type=str, required=True, default="['kiki','eden']")
    @use_kwargs({
        'participant': fields.Str(required=True, location='query'),
        'completion': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(marathonModel.get.model, code=200, mask=False)

    def get(self, participant, completion):
        hashalgorithm = HashAlgorithm()

        participant = participant[1:-1].split(",")
        completion = completion[1:-1].split(",")

        result = hashalgorithm.marathon(participant, completion)
        return result