def solution(n, lost, reserve):
    s = set()
    l = set(lost)
    r = set(reserve)

    for i in range(1, n+1):
        s.add(i)

    for v in l:
        if v in r:
            r.remove(v)
        elif v-1 in r and v-1 not in l:
            r.remove(v-1)
        elif v+1 in r and v+1 not in l:
            r.remove(v+1)
        else:
            s.remove(v)

    return len(s)
