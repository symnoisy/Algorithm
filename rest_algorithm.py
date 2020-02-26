import os
import threading
import secrets

from marshmallow import fields
from rest import programmers
from config_variable import logger
from flask_restplus.resource import Resource
from webargs.flaskparser import use_kwargs
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from time import gmtime, strftime

from service_programmers import HashAlgorithm, StackQueue, Heap
from service_programmers import Sorting, AbsoluteSearch, Greedy
from service_programmers import DynamicProgramming, DFSBFS_Search, BinarySearch, Graph

#HashModel (3/4)
from mgr_programmers import MarthonModel, PhoneBookModel, CamouflageModel
#Stack/Queue Model (2/6)
from mgr_programmers import TopModel, FunctionDevelopModel
#HeapModel (0/4)
#SortingModel (3/3)
from mgr_programmers import NumberKModel, BiggestNumberModel, HIndexModel
#AbsoluteSearchModel (1/4)
from mgr_programmers import MockTestModel
#Greedy Model (0/7)
#DynamicProgramming Model (0/7)
#DFS/BFS_Search Model (1/4)
from mgr_programmers import TargetNumberModel
#BinarySearch Model(0/3)
#Graph Model (0/4)


#Hash (3/4)
marathonModel = MarthonModel(programmers)
phoneBookModel = PhoneBookModel(programmers)
camouflageModel = CamouflageModel(programmers)
bestAlbumModel = '' #푸는중

#Stack/Queue (2/6)
topModel = TopModel(programmers)
functionDevelopModel = FunctionDevelopModel(programmers)

#Heap (0/4)

#Sorting (3/3)
numberKModel = NumberKModel(programmers)
biggestNumberModel = BiggestNumberModel(programmers)
hIndexModel = HIndexModel(programmers)

#AbsoluteSearch (1/4)
mockTestModel = MockTestModel(programmers)

#Greedy (0/7)
#DynamicProgramming (0/7)
#DFS/BFS_Search (1/4)
targetNumberModel = TargetNumberModel(programmers)

#BinarySearch (0/3)
#Graph (0/4)


#Hash REST API Service (3/4)
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

        participant = participant.replace("\'", "")
        participant = participant[1:-1].split(",")
        completion = completion.replace("\'", "")
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
        phoneBook = [int(data) for data in phoneBook]

        result = hashalgorithm.phoneBook(phoneBook)
        return result

@programmers.route('/hash/camouflage', methods=['GET'])
class ReturnAllChallenges(Resource):
    @programmers.doc(description='위장 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3')

    @programmers.param('clothes', '입을 수 있는 옷 경우의 수', _in = 'query', type = str, required = True, default = '[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]')
    @use_kwargs({
        'clothes': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(camouflageModel.get.model, code=200, mask=False)

    def get(self, clothes):
        hashalgorithm = HashAlgorithm()

        reformClothes = clothes[1:-1]
        reformClothes = reformClothes.replace("[", "")
        reformClothes = reformClothes.split("],")

        inputClothes = list()
        for clothe in reformClothes:
            clothe = clothe.replace(' ', '')
            clothe = clothe.replace('"', '')
            if "]" in clothe:
                clothe = clothe.replace("]", "")

            inputClothes.append(clothe.split(","))

        result = hashalgorithm.camouflage(inputClothes)
        return result


#Stack/Queue REST API Service (2/6)
@programmers.route('/stackqueue/top', methods=['GET'])
class ReturnTop(Resource):
    @programmers.doc(description='탑 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42588')
    @programmers.param('heights', '입력할 탑 리스트', _in='query', type=str, required=True, default="[6,9,5,7,4]")
    @use_kwargs({
        'heights': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(topModel.get.model, code=200, mask=False)
    def get(self, heights):
        stackqueue = StackQueue()

        heights = heights[1:-1].split(",")
        heights = [int(data) for data in heights]

        result = stackqueue.top(heights)

        return result

@programmers.route('/stackqueue/functiondevelop', methods=['GET'])
class ReturnTop(Resource):
    @programmers.doc(description='기능 개발 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42586')
    @programmers.param('progresses', '입력할 작업의 진도 리스트', _in='query', type=str, required=True, default="[93,30,55]")
    @programmers.param('speeds', '입력할 작업의 속도 리스트', _in='query', type=str, required=True, default="[1,30,5]")
    @use_kwargs({
        'progresses': fields.Str(required=True, location='query'),
        'speeds': fields.Str(required=True, location='query'),
    })
    @programmers.marshal_with(functionDevelopModel.get.model, code=200, mask=False)
    def get(self, progresses, speeds):
        stackqueue = StackQueue()

        progresses = progresses[1:-1].split(",")
        progresses = [int(data) for data in progresses]
        speeds = speeds[1:-1].split(",")
        speeds = [int(data) for data in speeds]

        result = stackqueue.functionDevelop(progresses, speeds)

        return result


#Heap REST API Service (0/4)


#Sorting REST API Service (3/3)
@programmers.route('/sorting/numberk', methods=['GET'])
class ReturnNumberK(Resource):
    @programmers.doc(description='K번째수 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42748')
    @programmers.param('array', '입력할 배열 리스트', _in='query', type=str, required=True, default="[1,5,2,6,3,7,4]")
    @programmers.param('commands', '입력할 commands 리스트', _in='query', type=str, required=True, default="[[2,5,3],[4,4,1],[1,7,3]]")
    @use_kwargs({
        'array': fields.Str(required=True, location='query'),
        'commands': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(numberKModel.get.model, code=200, mask=False)
    def get(self, array, commands):
        sorting = Sorting()

        array = array[1:-1].split(",")
        array = [int(data) for data in array]

        commands = commands[1:-1]
        commands = commands.replace("[", "")
        commands = commands.split("],")

        inputCommands = list()
        for command in commands:
            command = command.replace(' ', '')
            command = command.replace('"', '')
            if "]" in command:
                command = command.replace("]", "")

            tmp = command.split(",")
            tmp = [int(data) for data in tmp]
            inputCommands.append(tmp)

        result = sorting.numberK(array, inputCommands)

        return result

@programmers.route('/sorting/biggestnumber', methods=['GET'])
class ReturnBiggestNumber(Resource):
    @programmers.doc(description='가장 큰 수 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42746')
    @programmers.param('numbers', '입력할 정수 리스트', _in='query', type=str, required=True, default="[6,10,2]")
    @use_kwargs({
        'numbers': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(biggestNumberModel.get.model, code=200, mask=False)
    def get(self, numbers):
        sorting = Sorting()

        numbers = numbers[1:-1].split(",")
        numbers = [int(data) for data in numbers]

        result = sorting.biggestNumber(numbers)

        return result

@programmers.route('/sorting/hindex', methods=['GET'])
class ReturnHIndex(Resource):
    @programmers.doc(description='H-index 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42747')
    @programmers.param('citations', '입력할 인용횟수 리스트', _in='query', type=str, required=True, default="[3,0,6,1,5]")
    @use_kwargs({
        'citations': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(hIndexModel.get.model, code=200, mask=False)
    def get(self, citations):
        sorting = Sorting()

        citations = citations[1:-1].split(",")
        citations = [int(data) for data in citations]

        result = sorting.hIndex(citations)

        return result


#AbsoluteSearch REST API Service (1/4)
@programmers.route('/absolutesearch/mocktest', methods=['GET'])
class ReturnMockTest(Resource):
    @programmers.doc(description='모의고사 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/42840')
    @programmers.param('answers', '입력할 정답 리스트', _in='query', type=str, required=True, default="[1,2,3,4,5]")
    @use_kwargs({
        'answers': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(mockTestModel.get.model, code=200, mask=False)
    def get(self, answers):
        absoluteSearch = AbsoluteSearch()

        answers = answers[1:-1].split(",")
        answers = [int(data) for data in answers]

        result = absoluteSearch.mockTest(answers)

        return result

#Greedy REST API Service (0/7)
#DynamicProgramming REST API Service (0/7)
#DFS/BFS_Search REST API Service (1/4)
@programmers.route('/dfsbfs/targetnumber', methods=['GET'])
class ReturnMockTest(Resource):
    @programmers.doc(description='타겟 넘버 문제, '
                                 'https://programmers.co.kr/learn/courses/30/lessons/43165')
    @programmers.param('numbers', '입력할 사용할 숫자 리스트', _in='query', type=str, required=True, default="[1,1,1,1,1]")
    @programmers.param('target', '입력할 타겟 넘버 리스트', _in='query', type=str, required=True, default="3")
    @use_kwargs({
        'numbers': fields.Str(required=True, location='query'),
        'target': fields.Str(required=True, location='query')
    })
    @programmers.marshal_with(targetNumberModel.get.model, code=200, mask=False)
    def get(self, numbers, target):
        dFSBFS_Search = DFSBFS_Search()

        numbers = numbers[1:-1].split(",")
        numbers = [int(data) for data in numbers]
        target = int(target)

        result = dFSBFS_Search.targetNumber(numbers, target)

        return result

#BinarySearch REST API Service (0/3)
#Graph REST API Service (0/4)