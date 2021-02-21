import copy

def rotate(key):
    n = len(key)
    temp = copy.deepcopy(key)

    # 시계 방향으로 90도 회전
    for i in range(n):
        for j in range(n):
            temp[i][j] = key[n-j-1][i]
            
    return temp

def check(lock):
    count = 0
    size = len(lock)
    
    for i in range(size):
        count += lock[i].count(1)
    
    # lock이 1로 다 차있을 경우 True 반환
    if count == size*size:
        return True
    
    return False

def solution(key, lock):
    r = key

    for _ in range(4):
        # 시계방향 90도 회전
        r = rotate(r)

        # key 조정
        for y in range(1-len(lock),len(lock)):
            for x in range(1-len(lock),len(lock)):
                l = copy.deepcopy(lock)

                # lock과 key 검사
                for i in range(len(lock)):
                    for j in range(len(lock)):

                        # key 범위 검사
                        if i+y >=0 and i+y <len(r) and j+x >=0 and j+x <len(r):
                            l[i][j] += r[i+y][j+x]
        
                if check(l) == True:
                    return True

    return False