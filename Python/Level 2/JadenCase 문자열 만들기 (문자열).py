def solution(s):
    lst = s.split(' ')
    for i in range(len(lst)):
        # 문장의 맨 앞글자만 대문자로 변환하는 capitalize() 함수
        lst[i] = lst[i].capitalize()
    
    return (' ').join(lst)
    