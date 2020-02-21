import os
import threading
import secrets

from marshmallow import fields
from rest import programmers
from mgr_programmers import BiggestNumberModel, MarthonModel, PhoneBookModel
from config_variable import logger
from flask_restplus.resource import Resource
from webargs.flaskparser import use_kwargs
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from service_programmers import HashAlgorithm, Sorting
from time import gmtime, strftime

#Sorting
biggestModel = BiggestNumberModel(programmers)

#Hash
marathonModel = MarthonModel(programmers)
phoneBookModel = PhoneBookModel(programmers)

@programmers.route('/sorting/biggestnumber', methods=['GET'])
class ReturnBiggestNumber(Resource):
    @programmers.doc(description='가장 큰 수 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42746')
    @programmers.param('numbers', '입력할 정수 리스트', _in='query', type=str, required=True, default="[6,10,2]")
    @use_kwargs({
        'numbers': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(biggestModel.get.model, code=200, mask=False)
    def get(self, numbers):
        sorting = Sorting()

        numbers = numbers[1:-1].split(",")
        result = sorting.biggestNumber(numbers)

        return result


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


@programmers.route('/hash/phonebook', methods=['GET'])
class ReturnAllChallenges(Resource):
    @programmers.doc(description='전화번호부 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3')

    @programmers.param('phoneBook', '전화번호부', _in = 'query', type = str, required = True, default = "[119,97674223,1195524421]")
    @use_kwargs({
        'phoneBook': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(phoneBookModel.get.model, code=200, mask=False)

    def get(self, phoneBook):
        hashalgorithm = HashAlgorithm()

        phoneBook = phoneBook[1:-1].split(",")

        result = hashalgorithm.phoneBook(phoneBook)
        return result