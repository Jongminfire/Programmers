def solution(s):
    lst = []

    for i in s:
        if not lst or lst[-1] != i:
            lst.append(i)  
        else:
            lst.pop()
            
    return 0 if lst else 1
