import copy

from config_variable import logger

class Sorting:
    '''
    코딩테스트 연습 - 정렬
    '''

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

        resultRest['numbers'] = str(numbers)
        resultRest['result'] = str(int(''.join(f_list)))

        return resultRest

class HashAlgorithm:
    '''
    코딩테스트 연습 - 해시
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

            resultRest['result'] = str(participant[-1])
            return resultRest
        except:
            logger.error("Marathon job error. Participant=" + str(participant) + ", Completion=" + str(completion))
            return


    def phoneBook(self, phoneBook):
        '''
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

        logger.info("PhoneBook job start.")

        result_rest = dict()

        phoneBook.sort()
        phoneBook = [str(data) for data in phoneBook]

        result_rest['phoneBook'] = str(phoneBook)

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

        return result_rest