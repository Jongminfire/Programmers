def add_score(current_score,current_command,current_option,score_lst):
    command_list = ['S','D','T']

    if current_option == '*':
        if len(score_lst) >0:
            score_lst[len(score_lst)-1] *= 2
        score_lst.append(current_score ** (command_list.index(current_command)+1) * 2)

    elif current_option == '#':
        score_lst.append(-(current_score ** (command_list.index(current_command)+1)))

    else:
        score_lst.append(current_score ** (command_list.index(current_command)+1))


def solution(dartResult):
    score = []
    now = -1
    option = ''
    command = '' 
    
    for s in dartResult:
        if s.isdigit():
            if now == 1 and s == '0' and command == '':
                now = 10
            
            elif command.isalpha():
                add_score(now,command,option,score)
                
                command = ''
                option = ''
                now = int(s)
        
            else:
                now = int(s)
        
        elif s.isalpha():
            command = s
            
        else:
            option = s
    
    add_score(now,command,option,score)
    
    return sum(score)