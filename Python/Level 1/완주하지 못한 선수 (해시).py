def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i,v in enumerate(participant):
        if i >= len(completion) or v != completion[i]:
            return v