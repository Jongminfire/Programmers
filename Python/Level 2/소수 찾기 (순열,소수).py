from itertools import permutations

# 에라토스테네스의 체로 2부터 n+1까지 소수 찾기
def prime_list(n):
    sieve = [True] * (n+2)
    
    m = int((n+1) ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i , (n+1) , i):
                sieve[j] = False
                
    return [i for i in range(2,n+1) if sieve[i] == True]

def solution(numbers):
    prime = prime_list(int(''.join(sorted(numbers,reverse=True))))
    comb = set()
    cnt = 0
    for j in range(1,len(numbers)+1):
        for i in permutations(list(numbers),j):     # numbers에서 j만큼의 순열 뽑기
            comb.add(int(''.join(i)))

    for i in comb:
        if prime.count(i) > 0:
            cnt += 1

    return cnt