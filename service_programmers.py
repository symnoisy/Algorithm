import copy
import math

from config_variable import logger


class HashAlgorithm:
    '''
    코딩테스트 연습 - 해시 (3/4)
    '''

    def marathon(self, participant, completion):
        '''
        완주하지 못한 선수

        <문제 설명>
        수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
        마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
        완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

        <제한사항>
        마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
        completion의 길이는 participant의 길이보다 1 작습니다.
        참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
        참가자 중에는 동명이인이 있을 수 있습니다.

        입출력 예
        participant	completion	return
        [leo, kiki, eden]	[eden, kiki]	leo
        [marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
        [mislav, stanko, mislav, ana]	[stanko, ana, mislav]	mislav

        <입출력 예 설명>

        예제 #1
        leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

        예제 #2
        vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

        예제 #3
        mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

        :param completion:
        :return:
        '''

        resultRest = dict()

        try:
            logger.info("Marathon job start. Participant=" + str(participant) + ", Completion=" + str(completion))

            resultRest['participant'] = str(participant)
            resultRest['completion'] = str(completion)

            participant.sort()
            completion.sort()

            for i, j in zip(participant, completion):
                if i != j:
                    resultRest['result'] = str(i)
                    return resultRest

            result = participant[-1]
            resultRest['result'] = str(result)

            logger.info("Marathon job complete. Result=" + str(result))

            return resultRest
        except:
            logger.error("Marathon job error. Participant=" + str(participant) + ", Completion=" + str(completion))
            return


    def phoneBook(self, phoneBook):
        '''
        전화번호 목록

        <문제 설명>
        전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
        전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
        구조대 : 119
        박준영 : 97 674 223
        지영석 : 11 9552 4421
        전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
        어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

        <제한 사항>
        phone_book의 길이는 1 이상 1,000,000 이하입니다.
        각 전화번호의 길이는 1 이상 20 이하입니다.

        <입출력 예제>
        phone_book	                   return
        [119, 97674223, 1195524421]	    false
        [123,456,789]	                true
        [12,123,1235,567,88]	        false

        <입출력 예 설명>
        입출력 예 #1
        앞에서 설명한 예와 같습니다.

        입출력 예 #2
        한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

        입출력 예 #3
        첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

        :param participant:
        :param completion:
        :return:
        '''

        result_rest = dict()
        phoneBook.sort()

        try:
            logger.info("PhoneBook job start. Input=" + str(phoneBook))

            result_rest['phoneBook'] = str(phoneBook)

            phoneBook = [str(data) for data in phoneBook]

            for idxPhoneNumber, valuePhoneNumber in enumerate(phoneBook):
                tmpPhoneBook = copy.deepcopy(phoneBook)

                srcPhoneBook = tmpPhoneBook.pop(idxPhoneNumber)
                targetPhoneBook = [data[0:len(srcPhoneBook)] for data in tmpPhoneBook]
                targetPhoneBook = '_'.join(map(str, targetPhoneBook))

                if srcPhoneBook in targetPhoneBook:
                    result_rest['result'] = str(False)

                    logger.info("PhoneBook job complete. Result=" + str(result_rest))

                    return result_rest

            result_rest['result'] = str(True)

            logger.info("PhoneBook job complete. Result=" + str(result_rest))
        except:
            logger.error("PhoneBook job error. Input=" + str(phoneBook))
            return

        return result_rest


    def camouflage(self, clothes):
        '''
        위장

        <문제 설명>
        스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
        예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면
        다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

        종류	    이름
        얼굴	    동그란 안경, 검정 선글라스
        상의	    파란색 티셔츠
        하의	    청바지
        겉옷	    긴 코트

        스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

        <제한 사항>
        clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
        스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
        같은 이름을 가진 의상은 존재하지 않습니다.
        clothes의 모든 원소는 문자열로 이루어져 있습니다.
        모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
        스파이는 하루에 최소 한 개의 의상은 입습니다.

        <입출력 예>
        clothes	                                                                            return
        [[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	    5
        [[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	                3

        입출력 예 설명

        <예제 #1>
        headgear에 해당하는 의상이 yellow_hat, green_turban이고
        eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.
        1. yellow_hat
        2. blue_sunglasses
        3. green_turban
        4. yellow_hat + blue_sunglasses
        5. green_turban + blue_sunglasses

        <예제 #2>
        face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.
        1. crow_mask
        2. blue_sunglasses
        3. smoky_makeup
        :return:
        '''

        resultRest = dict()
        wear = dict()

        result = 1

        try:
            logger.info("Camouflage job start. Input=" + str(clothes))

            for clothe in clothes:

                category_wear = list(wear.keys())
                category = clothe[1]

                if category not in category_wear:
                    wear[category] = 2
                else:
                    wear[category] += 1

            for case in wear.keys():
                result = result * wear[case]
            result = result -1

            resultRest['clothes'] = str(clothes)
            resultRest['result'] = str(result)
            logger.info("Camouflage job complete. Result=" + str(result))
        except:
            logger.error("Camouflage job error. Input=" + str(clothes))
            return

        return resultRest


    def bestAlbum(self, genres, plays):
        '''
        베스트 앨범

        <문제 설명>
        스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
        노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
        속한 노래가 많이 재생된 장르를 먼저 수록합니다.
        장르 내에서 많이 재생된 노래를 먼저 수록합니다.
        장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
        노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
        베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

        <제한사항>
        genres[i]는 고유번호가 i인 노래의 장르입니다.
        plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
        genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
        장르 종류는 100개 미만입니다.
        장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
        모든 장르는 재생된 횟수가 다릅니다.

        <입출력 예>
        genres	                                 plays	                        return
        [classic, pop, classic, classic, pop]	[500, 600, 150, 800, 2500]	    [4, 1, 3, 0]

        <입출력 예 설명>
        classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
        고유 번호 3: 800회 재생
        고유 번호 0: 500회 재생
        고유 번호 2: 150회 재생

        pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
        고유 번호 4: 2,500회 재생
        고유 번호 1: 600회 재생

        따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.
        :param genres:
        :param plays:
        :return:
        '''

        result = list()
        dictGenre = dict()
        countGenre = dict()

        #key, value 생성
        for idx_genre, value_genre in enumerate(genres):
            if value_genre not in dictGenre.keys():
                dictGenre[value_genre] = dict()

                countGenre[value_genre] = plays[idx_genre]
                dictGenre[value_genre][idx_genre] = plays[idx_genre]
            else:
                countGenre[value_genre] += plays[idx_genre]
                dictGenre[value_genre][idx_genre] = plays[idx_genre]

        #정렬
        countGenre = sorted(countGenre.items(), reverse=True)
        print(countGenre)
        for genreName in countGenre:
            genreName = genreName[0]
            sortedPlay = sorted(dictGenre[genreName].items(), key=(lambda x:x[1]), reverse=True)
            if len(sortedPlay) == 1:
                result.append(sortedPlay[0][0])
            else:
                result.append(sortedPlay[0][0])
                result.append(sortedPlay[1][0])
        return result


class StackQueue:
    '''
    코딩테스트 연습 - 스택/큐 (2/6)
    '''

    def top(self, heights):
        '''
        탑

        <문제 설명>
        수평 직선에 탑 N대를 세웠습니다. 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치했습니다.
        발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신합니다. 또한, 한 번 수신된 신호는 다른 탑으로 송신되지 않습니다.
        예를 들어 높이가 6, 9, 5, 7, 4인 다섯 탑이 왼쪽으로 동시에 레이저 신호를 발사합니다.
        그러면, 탑은 다음과 같이 신호를 주고받습니다. 높이가 4인 다섯 번째 탑에서 발사한 신호는 높이가 7인 네 번째 탑이 수신하고,
        높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신합니다.
        높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신할 수 없습니다.

        송신 탑(높이)	    수신 탑(높이)
        5(4)	        4(7)
        4(7)	        2(9)
        3(5)	        2(9)
        2(9)	        -
        1(6)	        -

        맨 왼쪽부터 순서대로 탑의 높이를 담은 배열 heights가 매개변수로 주어질 때
        각 탑이 쏜 신호를 어느 탑에서 받았는지 기록한 배열을 return 하도록 solution 함수를 작성해주세요.

        <제한 사항>
        heights는 길이 2 이상 100 이하인 정수 배열입니다.
        모든 탑의 높이는 1 이상 100 이하입니다.
        신호를 수신하는 탑이 없으면 0으로 표시합니다.

        <입출력 예>
        heights	            return
        [6,9,5,7,4]	        [0,0,2,2,4]
        [3,9,9,3,5,7,2]	    [0,0,0,3,3,3,6]
        [1,5,3,6,7,6,5]	    [0,0,2,0,0,5,6]

        <입출력 예 설명>
        입출력 예 #1
        앞서 설명한 예와 같습니다.

        입출력 예 #2
        [1,2,3] 번째 탑이 쏜 신호는 아무도 수신하지 않습니다.
        [4,5,6] 번째 탑이 쏜 신호는 3번째 탑이 수신합니다.
        [7] 번째 탑이 쏜 신호는 6번째 탑이 수신합니다.

        입출력 예 #3
        [1,2,4,5] 번째 탑이 쏜 신호는 아무도 수신하지 않습니다.
        [3] 번째 탑이 쏜 신호는 2번째 탑이 수신합니다.
        [6] 번째 탑이 쏜 신호는 5번째 탑이 수신합니다.
        [7] 번째 탑이 쏜 신호는 6번째 탑이 수신합니다.

        :return:
        '''

        data = list()
        result = dict()

        try:
            logger.info("Top job start. Input=" + str(heights))

            for idx, height in enumerate(heights):
                target = heights[0:idx + 1]

                if len(target) == 1:
                    data.append(0)
                else:
                    find = 0

                    for idx2, receiver in enumerate(target):
                        sender = target[-1]

                        if idx2 == len(target) - 1:
                            continue
                        elif sender < receiver:
                            find = idx2 + 1
                        elif sender >= receiver:
                            continue

                    data.append(find)

            result['heights'] = str(heights)
            result['result'] = str(data)

            logger.info("Top job complete. Result=" + str(data))
        except:
            logger.error("Top job complete. Input=" + str(heights))
            return

        return result


    def functionDevelop(self, progresses, speeds):
        '''
        기능 개발

        <문제 설명>
        프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다.
        각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
        또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
        이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
        먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌
        정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

        <제한 사항>
        작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
        작업 진도는 100 미만의 자연수입니다.
        작업 속도는 100 이하의 자연수입니다.
        배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다.
        예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

        <입출력 예>
        progresses	    speeds	    return
        [93,30,55]	    [1,30,5]	[2,1]

        <입출력 예 설명>
        첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
        두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다.
        하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
        세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.
        따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

        :param progresses:
        :param speeds:
        :return:
        '''
        result = dict()

        spenddays = list()
        validate = list()
        answer = list()

        remain = [100 - progress for progress in progresses]

        try:
            logger.info("FunctionDevelop job start. Input=" + str(progresses) + str(speeds))

            for idx, speed in enumerate(speeds):
                calc = math.ceil(remain[idx] / speed)
                spenddays.append(calc)
                validate.append(calc)

            file = 1
            king = spenddays.pop(0)

            while len(spenddays) > 0:
                release = king
                candidate = spenddays[0]

                if king >= candidate:
                    file += 1
                    spenddays.pop(0)
                elif release < candidate:
                    king = candidate
                    answer.append(file)
                    spenddays.pop(0)
                    file = 1

            answer.append(file)

            result['progresses'] = str(progresses)
            result['speeds'] = str(speeds)
            result['result'] = str(answer)

            logger.info("FunctionDevelop job complete. Result=" + str(progresses) + str(speeds))
        except:
            logger.error("FunctionDevelop job error. Input=" + str(progresses, speeds))
            return

        return result


class Heap:
    '''
    코딩테스트 연습 - 힙 (0/4)
    '''
    def __init__(self):
        sample = 1


class Sorting:
    '''
    코딩테스트 연습 - 정렬 (3/3)
    '''


    def numberK(self, array, commands):
        '''
        k번째 수

        <문제 설명>
        배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
        예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
        array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
        1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
        2에서 나온 배열의 3번째 숫자는 5입니다.
        배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
        commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

        <제한사항>
        array의 길이는 1 이상 100 이하입니다.
        array의 각 원소는 1 이상 100 이하입니다.
        commands의 길이는 1 이상 50 이하입니다.
        commands의 각 원소는 길이가 3입니다.

        <입출력 예>
        array	                    commands	                            return
        [1, 5, 2, 6, 3, 7, 4]	    [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	    [5, 6, 3]

        <입출력 예 설명>
        [1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
        [1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
        [1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.
        :param array:
        :param commands:
        :return:
        '''

        resultRest = dict()

        result = []

        try:
            logger.info("NumberK job start. Input=" + str(array) + str(commands))

            for command_list in commands:
                managed_list = array[command_list[0] - 1: command_list[1]]
                managed_list.sort()
                result.append(managed_list[command_list[2] - 1])

            resultRest['array'] = str(array)
            resultRest['commands'] = str(commands)
            resultRest['result'] = str(result)

            logger.info("NumberK job complete. Result=" + str(result))
        except:
            logger.error("NumberK job error. Input=" + str(array) + str(commands))
            return

        return resultRest


    def biggestNumber(self, numbers):
        '''
        가장 큰 수

        <문제 설명>
        0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
        예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
        이중 가장 큰 수는 6210입니다.
        0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
        순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

        <제한 사항>
        numbers의 길이는 1 이상 100,000 이하입니다.
        numbers의 원소는 0 이상 1,000 이하입니다.
        정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

        <입출력 예>
        numbers 	            return
        [6, 10, 2] 	            "6210"
        [3, 30, 34, 5, 9] 	    "9534330"

        :return:
        '''

        resultRest = dict()

        com_list = []
        f_list = []

        try:
            logger.info("BiggestNumber job start. Input=" + str(numbers))

            resultRest['numbers'] = str(numbers)

            numbers = [str(i) for i in numbers]

            for i in numbers:
                if len(i) == 4:
                    com_list.append([i, i * 3])
                if len(i) == 3:
                    com_list.append([i, i * 4])
                if len(i) == 2:
                    com_list.append([i, i * 6])
                if len(i) == 1:
                    com_list.append([i, i * 12])

            com_list.sort(key=lambda x: x[1], reverse=True)

            for i in com_list:
                f_list.append(i[0])

            result = int(''.join(f_list))
            resultRest['result'] = str(result)

            logger.info("BiggestNumber job complete. Result=" + str(result))
        except:
            logger.error("BiggestNumber job error. Input=" + str(numbers))
            return

        return resultRest


    def hIndex(self, citations):
        '''
        H-Index

        <문제 설명>
        H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
        어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
        위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
        어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
        나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.
        어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
        이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

        <제한사항>
        과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
        논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

        <입출력 예>
        citations	       return
        [3, 0, 6, 1, 5]	    3

        <입출력 예 설명>
        이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다.
        그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.
        :return:
        '''

        resultRest = dict()

        result = 0

        try:
            logger.info("HIndex job start. Input=" + str(citations))

            resultRest['citations'] = str(citations)

            citations.sort()
            lenCitations = len(citations)
            for i in range(lenCitations):
                if citations[i] >= lenCitations-i:
                    result = lenCitations-i

                    resultRest['result'] = str(result)
                    return resultRest

            resultRest['result'] = str(result)
            logger.info("HIndex job start. Result=" + str(result))
        except:
            logger.error("HIndex job error. Input=" + str(citations))
            return

        return resultRest


class AbsoluteSearch:
    '''
    코딩테스트 연습 - 완전탐색 (1/4)
    '''
    def mockTest(self, answers):
        '''
        모의고사

        <문제 설명>
        수포자는 수학을 포기한 사람의 준말입니다.
        수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
        수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
        1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
        2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
        3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
        1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
        가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

        <제한 조건>
        시험은 최대 10,000 문제로 구성되어있습니다.
        문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
        가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

        <입출력 예>
        answers	        return
        [1,2,3,4,5]	    [1]
        [1,3,2,4,2]	    [1,2,3]

        <입출력 예 설명>
        입출력 예 #1
        수포자 1은 모든 문제를 맞혔습니다.
        수포자 2는 모든 문제를 틀렸습니다.
        수포자 3은 모든 문제를 틀렸습니다.
        따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

        입출력 예 #2
        모든 사람이 2문제씩을 맞췄습니다.
        :param answers:
        :return:
        '''

        resultRest = dict()

        result = []
        scores = []
        students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

        try:
            logger.info("MockTest job start. Input=" + str(answers))

            resultRest['answers'] = str(answers)

            for idx, student in enumerate(students):
                lengap = math.ceil(len(answers) / len(student))

                if lengap != 1:
                    students[idx] = student * lengap

            for student in students:
                studentscore = 0

                for idx, answer in enumerate(answers):
                    if answer == student[idx]:
                        studentscore += 1
                    if idx == len(answers) - 1:
                        scores.append(studentscore)

            bestscore = max(scores)
            for idx, score in enumerate(scores):
                if scores[idx] == bestscore:
                    result.append(idx + 1)

            resultRest['result'] = str(result)

            logger.info("MockTest job start. Result=" + str(result))
        except:
            logger.error("MockTest job error. Input=" + str(answers))
            return

        return resultRest

class Greedy:
    '''
    코딩테스트 연습 - 탐욕법 (0/7)
    '''
    def __init__(self):
        sample = 1


class DynamicProgramming:
    '''
    코딩테스트 연습 - 동적계획 (0/7)
    '''
    def __init__(self):
        sample = 1


class DFSBFS_Search:
    '''
    코딩테스트 연습 - 깊이/너비 우선 탐색 (1/4)
    '''
    def targetNumber(self, numbers, target):
        '''
        타겟 넘버

        <문제 설명>
        n개의 음이 아닌 정수가 있습니다.
        이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
        예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3
        사용할 수 있는 숫자가 담긴 배열 numbers,
        타겟 넘버 target이 매개변수로 주어질 때
        숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

        <제한사항>
        주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
        각 숫자는 1 이상 50 이하인 자연수입니다.
        타겟 넘버는 1 이상 1000 이하인 자연수입니다.

        <입출력 예>
        numbers	            target	    return
        [1, 1, 1, 1, 1]	    3	        5
        :return:
        '''

        resultRest = dict()

        result = 0
        len_numbers = len(numbers)

        try:
            logger.info("TargetNumber job start. Input1=" + str(numbers) + ", Input2=" + str(target))

            resultRest['numbers'] = str(numbers)
            resultRest['target'] = str(target)

            def operator(idx=0):
                if idx < len_numbers:
                    numbers[idx] *= 1
                    operator(idx + 1)

                    numbers[idx] *= -1
                    operator(idx + 1)

                elif sum(numbers) == target:
                    nonlocal result
                    result += 1

            operator()

            resultRest['result'] = str(result)

            logger.info("TargetNumber job start. Result=" + str(result))
        except:
            logger.error("TargetNumber job error. Input1=" + str(numbers) + ", Input2=" + str(target))
            return

        return resultRest


class BinarySearch:
    '''
    코딩테스트 연습 - 이분탐색 (0/3)
    '''
    def __init__(self):
        sample = 1


class Graph:
    '''
    코딩테스트 연습 - 그래 (0/4)
    '''
    def __init__(self):
        sample = 1