def solution(brown, yellow):
    # yellow가 1이상이므로 카펫의 최소 길이 3부터 약수검사
    for i in range(3,(brown+yellow)//3+1):
        if (brown+yellow) % i == 0:
            x = i
            y = (brown+yellow)/i
            
            if 2*(x+y-2) == brown:
                return sorted([x,y], reverse = True)