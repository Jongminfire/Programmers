def solution(scores):
    answer = ''
    newScores = list(map(list, zip(*scores)))   # 2차원 리스트 행열 뒤집기
    length = len(newScores)
    
    def alpha(num):
        if num >= 90:
            return 'A'
        elif 80 <= num < 90:
            return 'B'
        elif 70 <= num < 80:
            return 'C'
        elif 50 <= num < 70:
            return 'D'
        else:
            return 'F'
    
    for i in range(0,length):
        sumScore = sum(newScores[i])
        maxScore = max(newScores[i])
        minScore = min(newScores[i])
        count = length
        
        # 가장 큰, 가장 작은 값이 하나고 자기 자신을 평가한 점수일 때 제외
        if (newScores[i].count(maxScore) == 1 and maxScore == newScores[i][i]):
            sumScore -= maxScore
            count -= 1
        if (newScores[i].count(minScore) == 1 and minScore == newScores[i][i]):
            sumScore -= minScore
            count -= 1
        
        answer += alpha(sumScore//count)
        
    return answer