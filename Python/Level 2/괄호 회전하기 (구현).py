def check(s):
    stack = []

    for i in s:
        # 괄호를 여는 문자면 stack에 append
        if i in ['[', '(', '{']:
            stack.append(i)
        else:
            # stack이 비었거나 괄호의 짝이 맞지 않으면 False 반환
            if not stack or (stack[-1] == '[' and i != ']') or (stack[-1] == '{' and i != '}') or (stack[-1] == '(' and i != ')'):
                return False
            stack.pop()

    return True if not stack else False


def solution(s):
    cnt = 0

    for _ in range(len(s)):
        if check(s):
            cnt += 1

        s = s[1:]+s[0]

    return cnt
