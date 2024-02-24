class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        peopleWithSecret = [0,firstPerson]
        sortedMeetings = sorted(meetings, key = lambda x: x[2])
        sortedMeetings.insert(0,[0,firstPerson,0])
        answer = []

        for item in sortedMeetings:
            if item[0] and item[1] in peopleWithSecret:
                continue
            elif item[0] in peopleWithSecret:
                peopleWithSecret.append(item[1])
            elif item[1] in peopleWithSecret:
                peopleWithSecret.append(item[0])
            else:
                continue

        for item in peopleWithSecret:
            if item not in answer:
                answer.append(item)

        return answer
