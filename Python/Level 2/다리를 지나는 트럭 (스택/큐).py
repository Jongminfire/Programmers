from collections import deque

def solution(bridge_length, weight, truck_weights):
    dq = deque(truck_weights)
    bridge = deque([])
    bridge_time = deque([])
    sec = 0
    
    while dq:
        if not bridge:
            bridge.append(dq[0])
            bridge_time.append(1)
            dq.popleft()
            sec += 1

            continue

        if bridge_time[0] == bridge_length:
            bridge.popleft()
            bridge_time.popleft()
        
        if sum(bridge) + dq[0] <= weight:
            bridge.append(dq[0])
            bridge_time.append(0)
            dq.popleft()
            sec += 1

            for i in range(len(bridge_time)):
                bridge_time[i] += 1
                
        else:
            move = bridge_length-bridge_time[0]

            bridge.popleft()
            bridge_time.popleft()

            sec += move
            for i in range(len(bridge_time)):
                bridge_time[i] += move
            

    return sec + bridge_length - bridge_time[-1]+1

# bridge와 bridge_time을 2차원 리스트로 묶거나 하는 방법으로 코드 길이 줄일 수 있을 듯