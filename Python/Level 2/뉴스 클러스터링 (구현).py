from collections import defaultdict


def solution(str1, str2):
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    str1 = str1.lower()
    str2 = str2.lower()

    inter = 0   # 교집합
    union = 0   # 합집합

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            dict1[str1[i:i+2]] += 1

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            dict2[str2[i:i+2]] += 1

    for i in dict1:
        if i in dict2:
            inter += min(dict1[i], dict2[i])
            union += max(dict1[i], dict2[i])
        else:
            union += dict1[i]

    for i in dict2:
        # dict2에 있고 dict1에 없는 값 합집합 크기로 더해주기
        if i not in dict1:
            union += dict2[i]

    # 합집합이 0일 경우 65536
    return int((inter/union)*65536) if union != 0 else 65536
