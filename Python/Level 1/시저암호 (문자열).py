def solution(s, n):
    answer = ""
    
    for i in s:
        temp = 32
        if i.isalpha():
            if ord(i) <= 96:
                temp = 65+(ord(i)+n-65)%26
            else:
                temp = 97+(ord(i)+n-97)%26
        answer += chr(temp)
        
    return answer