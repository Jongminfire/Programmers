from collections import defaultdict


# 주어진 문자열 중 사전에 있는 문자 찾기
def check(msg, dic, msg_idx):
    result = msg[msg_idx]
    temp = ''

    for i in range(msg_idx, len(msg)):
        temp += msg[i]
        if temp in dic:
            result = temp

    return result


def solution(msg):
    dic = defaultdict(int)
    idx = 1
    msg_idx = 0
    ans = []

    # A-Z까지 사전 등록
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dic[i] = idx
        idx += 1

    while msg_idx < len(msg):
        result = check(msg, dic, msg_idx)
        msg_idx += len(result)

        # 사전에 등록되어 있는 값 추가
        ans.append(dic[result])

        # 방금 추가한 값과 바로 뒤에 오는 문자가 사전에 없을 경우 사전에 추가
        if msg_idx < len(msg)-1 and result+msg[msg_idx] not in dic:
            dic[result+msg[msg_idx]] = idx
            idx += 1

    return ans
