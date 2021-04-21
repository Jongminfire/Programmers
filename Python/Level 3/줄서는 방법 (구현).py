def check(n, k, lst, ans):
    # 리스트의 순서대로 답을 넣으므로 정렬
    lst.sort()
    scope = 1

    # n값에 따라 범위 찾기 (1,2,6,24,120..)
    for i in range(1, n-1):
        scope *= (i+1)

    for i in range(n):
        # k가 해당 범위에 있으면 남은 리스트의 i번째를 ans 리스트에 추가
        if i*scope <= k <= (i+1)*scope-1:
            ans.append(lst[i])
            lst.remove(lst[i])
            check(n-1, k-i*scope, lst, ans)

    return ans


def solution(n, k):
    return check(n, k-1, [i for i in range(1, n+1)], [])

# itertools의 permutation으로는 효율성 넘기지 못해서 재귀로 구현함
