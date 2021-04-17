# 균형잡힌 괄호 문자열 반환

def balanced(s):
    cnt = 0
    u = ''
    w = ''

    for i, v in enumerate(s):
        if v == '(':
            cnt += 1
        elif v == ')':
            cnt -= 1

        if cnt == 0:
            u = s[:i+1]
            w = s[i+1:]
            break

    if not u:
        u = s

    return u, w


# 올바른 괄호 문자열 검사

def right_check(s):
    cnt = 0

    for i in s:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1

    return True if cnt == 0 else False


# 첫번쨰와 마지막 문자를 제거하고 괄호 방향 뒤집기

def reverse(s):
    s = s[1:-1]
    result = ''

    for i in s:
        if i == ')':
            result += '('
        else:
            result += ')'

    return result


# 1단계부터 재귀

def recursive(p):
    ans = ''
    u = ''
    v = ''
    temp = ''

    while p:
        u, v = balanced(p)

        if right_check(u):
            ans += u
            p = v
        else:
            temp = '('+recursive(v)+')'+reverse(u)
            break

    return ans + temp


def solution(p):
    # 빈 문자열 인 경우 빈 문자열 반환, 아닐 경우 과정 실행
    return recursive(p) if p else p
