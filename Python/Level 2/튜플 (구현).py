def solution(s):
    ans = []

    # 양쪽 괄호 제거
    while s[1] == '{':
        s = s[1:-1]

    # 괄호로 나뉜 부분 제거
    s = s.split('},{')

    # 첫번째와 마지막 괄호 제거
    s[0] = s[0][1:]
    s[-1] = s[-1][:-1]

    # 길이 순서대로 정렬
    for i in sorted(s, key=lambda x: len(x)):
        num = i.split(',')

        for n in num:
            # n이 답에 없을 경우 ans에 넣음
            if int(n) not in ans:
                ans.append(int(n))
                break

    return ans
