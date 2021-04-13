def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        lst = []
        for j in range(len(arr2[0])):
            num = 0
            for x in range(len(arr1[0])):
                num += arr1[i][x] * arr2[x][j]
                
            lst.append(num)
        answer.append(lst)
          
    return answer