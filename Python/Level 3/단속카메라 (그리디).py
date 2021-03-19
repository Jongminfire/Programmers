def solution(routes):
    cnt = 0
    
    camera = min(routes)[0]-1               # 초기 카메라는 제일 빠른 시작위치 -1
    routes.sort(key = lambda x : x[1])      # 끝나는 위치 기준으로 정렬

    for i in routes:
        if camera < i[0]:
            camera = i[1]                   # 카메라가 시작점보다 작을경우 갱신
            cnt += 1

    return cnt