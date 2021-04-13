from collections import deque

def solution(priorities, location):
    dq = deque()
    cnt = 0
    i = -1
    
    for i in range(len(priorities)):
        dq.append((priorities[i],i))

    while dq:
        v,i = dq.popleft()

        if dq and max(dq)[0] > v:
            dq.append((v,i))
        else:
            cnt += 1

            if i == location:
                break

    return cnt