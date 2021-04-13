def solution(n, words):
    answer = [0,0]
    prev = words[0]
    # 검색을 빠르게 하기 위해 dictionary 사용
    word = {words[0]:1}
    
    for i in range(1,len(words)):
        if words[i][0] != prev[-1] or words[i] in word :
            answer = [i%n+1,i//n+1]
            break
        else:
            prev = words[i]
            word[words[i]]=1

    return answer