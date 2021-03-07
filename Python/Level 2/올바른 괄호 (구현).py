def solution(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            else:
                cnt -= 1
    
    return True if cnt == 0 else False