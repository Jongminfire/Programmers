def solution(s):
    size = len(s)
    answer = len(s)

    # 절반 이상이 넘는 범위는 줄일 수 없으므로 size//2 + 1 까지
    for i in range(1,size//2+1):
        idx = 0
        count = 1
        value = size
        prev = ""

        while idx < size:
            # i의 범위만큼 확인
            now = s[idx:idx+i]

            if prev == now:
                # 처음 겹치는 경우는 숫자 포함하기 때문에 -1
                if count == 1:
                    value -= (i-1)
                else:
                    value -= i
                count += 1
                
                # count의 자리수가 바뀔 경우 추가로 더해줌
                if count == 10:
                    value += 1
            else:
                count = 1
            prev = now
            idx += i

        answer = min(answer,value)
        
    return answer