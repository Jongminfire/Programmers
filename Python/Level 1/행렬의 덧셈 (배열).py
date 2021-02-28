def solution(arr1, arr2):
    answer = []
    for i in range (len(arr1)):
        lst = []
        for j in range (len(arr1[0])):
            lst.append(arr1[i][j]+arr2[i][j])
        answer.append(lst)
    return answer