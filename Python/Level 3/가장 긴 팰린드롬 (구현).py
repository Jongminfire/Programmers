# 뒤집어도 같은 문자인지 체크
def check(s):
    return len(s) if s == s[::-1] else False


def solution(s):
    # 범위가 긴 순서대로 검사
    for i in range(len(s), 0, -1):
        for j in range(0, len(s)-i+1):
            if check(s[j:j+i]):
                return check(s[j:j+i])
