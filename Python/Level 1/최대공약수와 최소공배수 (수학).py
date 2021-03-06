from math import gcd

def solution(n, m):
    # gcd(n,m)으로 최대공약수를 구할 수 있다
    # 최소공배수는 n*m를 최대공약수로 나눈 값
    answer = [gcd(n,m),(n*m)//gcd(n,m)]
    return answer