def solution(clothes):
    cloth = {}
    cnt = 1

    for i in clothes:
        if i[1] in cloth:
            cloth[i[1]] += 1
        else:
            cloth[i[1]] = 1
    
    for i in cloth:
        cnt *= (cloth[i] + 1)

    # 옷을 입는 모든 가짓수는 (종류 개수+1)의 곱에서 모두 안 입는 경우인 1을 제거
    return cnt - 1