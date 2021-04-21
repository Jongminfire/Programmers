def solution(n, times):
    times.sort()

    # 탐색 범위를 0부터 가장 긴 심사관에게 모두 받는 경우까지로 정함
    left = 0
    right = max(times) * (len(times)+1)

    while left <= right:
        mid = (left+right) // 2
        cnt = 0

        for t in times:
            cnt += mid//t

            if cnt >= n:
                break

        if cnt < n:
            left = mid + 1
        else:
            right = mid - 1

    return left
