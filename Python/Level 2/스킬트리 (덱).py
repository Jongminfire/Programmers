from collections import deque
import copy

def check(skill,order):
    for i in skill:
        if i in order:
            if i != order.popleft():
                return False
    return True


def solution(skill, skill_trees):
    order = list(skill)
    ans = 0
    
    for i in skill_trees:
        if check(i,deque(copy.deepcopy(order))) == True:
            ans += 1
    
    return ans