def solution(record):
    user = {}
    answer = []
    
    for i in record:
        command = i.split()
        
        if len(command) == 3:
            user[command[1]] = command[2]
    
    for i in record:
        command = i.split()
        
        if command[0] == 'Enter':
            answer.append(user[command[1]]+'님이 들어왔습니다.')
        elif command[0] == 'Leave':
            answer.append(user[command[1]]+'님이 나갔습니다.')
    
    return answer