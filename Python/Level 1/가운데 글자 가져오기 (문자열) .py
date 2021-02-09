def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[len(s)//2-1]+s[len(s)//2]
    else:
        answer = s[len(s)//2]
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
# 문자열 길이에 따라 가운데 글자 반환