def solution(arr):
    ans = [0, 0]

    # 압축 필요 검사
    def check(arr, x, y, size):
        cnt = 0

        for i in arr[x:x+size]:
            cnt += sum(i[y:y+size])

        return True if cnt == 0 or cnt == size**2 else False

    # 쿼드트리 재귀 함수
    def compress(arr, x, y, size):
        # 압축 필요 없으면 단일 개수로 증가
        if check(arr, x, y, size):
            ans[arr[x][y]] += 1

        # 네 구간으로 압축
        else:
            compress(arr, x, y, size//2)
            compress(arr, x, y+size//2, size//2)
            compress(arr, x+size//2, y, size//2)
            compress(arr, x+size//2, y+size//2, size//2)

    compress(arr, 0, 0, len(arr))

    return ans
