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