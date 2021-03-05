def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range (len(citations)):
        if citations[i] >= len(citations) - i:
            answer = max(len(citations)-i,answer)
    
    return answer