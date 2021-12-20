def solution(s):
    answer = ''
    idx = 0
    
    for word in s:
        if word == ' ':
            idx = 0
            answer += ' '
        else:
            answer += word.upper() if not idx % 2 else word.lower()
            idx += 1
    
    return answer