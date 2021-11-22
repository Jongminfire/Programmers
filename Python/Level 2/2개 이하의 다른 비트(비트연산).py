def solution(numbers):    
    def bit_check(num):
        if num % 2 == 0:
            return num+1
        else:
            lastBit = ~num & (num+1)
            return (num|lastBit) & ~(lastBit>>1)
    
    return [bit_check(num) for num in numbers]