def solution(arr):
    answer = [arr[0]]
    
    for i in arr:
        if i != answer[-1]:         # answer[len(answer)-1] 대신 answer[-1]를 쓰자
            answer.append(i)
            
    return answer