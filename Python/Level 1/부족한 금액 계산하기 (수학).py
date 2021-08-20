def solution(price, money, count):
    countSum = (count+1) * count//2
    ans = price*countSum - money

    return ans if ans > 0 else 0