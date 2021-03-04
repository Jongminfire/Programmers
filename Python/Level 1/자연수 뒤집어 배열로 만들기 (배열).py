def solution(n):
    lst = []
    for i in range(len(str(n))-1,-1,-1):
        lst.append(int(str(n)[i]))
    return lst

"""
map함수를 이용한

return list(map(int,reversed(str(n))))

이나

return [int(i) for i in str(n)][::-1]

같은 방법도 있음
"""
