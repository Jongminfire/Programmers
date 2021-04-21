# 이분 탐색으로 lower_bound 구현
def lower_bound(works, target):
    left = 0
    right = len(works)-1

    while left <= right:
        mid = (left+right)//2

        if works[mid] > target:
            left = mid + 1
        elif works[mid] <= target:
            right = mid - 1

    return right+1


def solution(n, works):
    works.sort(reverse=True)
    ans = 0
    if sum(works) < n:
        return 0

    while n != 0:
        lower = lower_bound(works, works[0]-1)

        # 가장 큰 값 모두를 1씩 감소 시킬 수 있을 때
        if n > lower:
            n -= lower
            works[:lower] = [works[0]-1 for _ in range(lower)]

        # n이 가장 큰 값의 개수보다 작을 때 total과 remain으로 나눠서 계산
        else:
            total = n//lower
            remain = n % lower

            works[:lower] = [works[0] - (total) for _ in range(lower)]
            works[:remain] = [works[0]-1 for _ in range(remain)]
            break

    for i in works:
        ans += i**2

    return ans

# 이분탐색 대신 heapq로 구현하면 더 간단하게 구할 수 있을 듯
