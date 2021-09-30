def solution(sizes):
    ans = [0,0]
    
    for i,v in enumerate(sizes):
        sizes[i].sort(reverse=True)
    
    for v in sizes:
        ans[0] = max(ans[0],v[0])
        ans[1] = max(ans[1],v[1])
    
    return ans[0]*ans[1]