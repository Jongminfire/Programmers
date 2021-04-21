def solution(n, s):
    total = s//n
    remain = s % n

    if s < n:
        return [-1]

    ans = [total for _ in range(n-remain)]
    ans += [total+1 for _ in range(remain)]

    return sorted(ans)
