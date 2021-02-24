def dfs(start,numbers,target,cnt):
    if start == len(numbers):
        if cnt == target:
            return 1
        else:
            return 0

    # 합과 차 두 가지의 경우로 나눔    
    cal1 = cnt + numbers[start]
    cal2 = cnt - numbers[start]
    
    # 두 경우로 재귀
    return dfs(start+1,numbers,target,cal1)+dfs(start+1,numbers,target,cal2)

def solution(numbers, target):
    return dfs(0,numbers,target,0)