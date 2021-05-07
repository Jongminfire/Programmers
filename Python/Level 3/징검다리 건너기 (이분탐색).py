INF = int(1e9)


def solution(stones, k):
    left = 0
    right = INF  # 건널 수 있는 친구의 수는 무제한

    while left <= right:
        mid = (left+right)//2
        cnt = 0

        for s in stones:
            if s-mid <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:    # 카운트가 k보다 같거나 크면 건널 수 없음
                break

        if cnt >= k:
            right = mid-1
        else:
            left = mid+1

    return left
