import re,copy

def solution(expression):
    num = re.split(r'\W+',expression)           # /W 는 알파벳,숫자,'_' 가 아닌 문자를 의미함
    car = re.split(r'\w+',expression)[1:-1]     # /w 는 알파벳,숫자,'_' 인 문자를 의미함
    order = [
        ['+','-','*'],
        ['+','*','-'],
        ['-','+','*'],
        ['-','*','+'],
        ['*','+','-'],
        ['*','-','+']
    ]
    ans = 0
    
    for i in order:
        copynum = list(map(int,copy.deepcopy(num)))
        copycar = copy.deepcopy(car)
        
        for j in i:
            while j in copycar:
                index = copycar.index(j)
                
                if j == '+':
                    value = copynum[index] + copynum[index+1]
                elif j == '-':
                    value = copynum[index] - copynum[index+1]
                else:
                    value = copynum[index] * copynum[index+1]
                    
                copycar.remove(j)
                copynum[index] = value
                del copynum[index+1]
        
        ans = max(ans,abs(copynum[0]))
    
    return ans