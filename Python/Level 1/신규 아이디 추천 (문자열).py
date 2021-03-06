def solution(new_id):
    answer = new_id.lower()
    save = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-','_','.']

    for i in answer:
        if i not in save:
            answer = answer.replace(i,"")

    while answer.find("..") != -1:
        answer = answer.replace("..",".")
        
    if answer[0] == ".":
        answer = answer[1:]
    if len(answer) == 0:
        answer = "a"
    if answer[-1] == ".":
        answer = answer[:-1]
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]

    return answer