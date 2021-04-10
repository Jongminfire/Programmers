from collections import deque

def solution(progresses, speeds):
    prog = deque(progresses)
    spd = deque(speeds)
    answer = []
    day = 0
    
    while prog:
        cnt = 0
        
        while prog[0] < 100:
            day += 1
            
            for i in range(len(prog)):
                prog[i] += spd[i]
        
        while prog[0] >= 100:
            prog.popleft()
            spd.popleft()
            cnt += 1
            
            if not prog:
                break
        
        answer.append(cnt)

    return answer