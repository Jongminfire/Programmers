def solution(n):
    temp = ''

    # 10진법 → 3진법 (앞 뒤 반전)
    while n > 0:
        n, mod = divmod(n, 3)
        temp += str(mod)

    return int(temp, 3)  # 3진법 → 10진법
