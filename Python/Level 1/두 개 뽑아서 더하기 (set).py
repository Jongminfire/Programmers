def solution(numbers):
    s = set()
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if i != j:
                s.add(numbers[i]+numbers[j])
    answer = list(s)
    
    # python의 set은 해시셋이기 때문에 list(set())은 정렬된 리스트를 보장하지 않음.
    answer.sort()
    return answer