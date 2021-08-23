def solution(n, k, cmd):
    answer = ['O'] * (n)
    linked = {i:[i-1,i+1] for i in range(n)}    # prev,next의 노드로 이루어진 연결리스트로 구현
    deleted = []    # 삭제된 정점을 저장하는 배열 (스택)
    now = k
    
    for command in cmd:
        if command == 'C':
            if linked[now][0] != -1:    # 정점 now가 head가 아닐 경우
                linked[linked[now][0]][1] = linked[now][1]
            if linked[now][1] != n:     # 정점 now가 tail이 아닐 경우
                linked[linked[now][1]][0] = linked[now][0]

            answer[now] = 'X'   # 삭제 정점의 정답은 X
            deleted.append(now)
            
            if linked[now][1] == n:     # 정점 now가 tail일 경우 now는 이전 정점
                now = linked[now][0]
            else:
                now = linked[now][1]
                
        elif command == 'Z':
            idx = deleted.pop()
            answer[idx] = 'O'   # 되돌린 정점의 정답은 O
            
            if linked[idx][0] != -1:    # 정점 idx가 head가 아닐 경우
                linked[linked[idx][0]][1] = idx
            if linked[idx][1] != n:     # 정점 idx가 tail이 아닐 경우
                linked[linked[idx][1]][0] = idx
            
        else:
            c,num = command.split()
            
            # num만큼 연결리스트내에서 반복 이동
            if c == 'U':                
                for _ in range(int(num)):
                    now = linked[now][0]
            else:
                for _ in range(int(num)):
                    now = linked[now][1]
        
    return ''.join(answer)