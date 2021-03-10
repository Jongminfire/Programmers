def solution(name):
    idx = []
    cnt = 0
    
    # 알파벳 조정하는 개수 세기
    for i in range(len(name)):
        asc = ord(name[i])
        # 위로 올리는 횟수와 아래로 내리는 횟수 중 적은 수 세기
        cnt += min((asc-ord('A')),(ord('Z')-asc+1))  
    
    # A가 아닌 알파벳 인덱스 얻기
    for i in range(len(name)):
        if name[i] != 'A':
            idx.append(i)
    
    # 움직이는 거리 기본 값은 오른쪽으로 이동하는 경우
    dist = idx[-1]
    
    # 이동하다 중간에 왼쪽으로 이동하는 경우와 dist의 대소비교
    for i in range(len(idx)-1):
        dist = min(2*idx[i]+len(name)-idx[i+1],dist)

    return dist + cnt