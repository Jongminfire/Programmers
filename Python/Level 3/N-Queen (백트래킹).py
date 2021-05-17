cnt = 0


def solution(n):
    init = {i for i in range(n)}

    def queen_check(sol, size):
        global cnt

        if size == n:
            cnt += 1
            return 0

        candidate = init - set(sol)

        for c in candidate:
            check = True
            for i, v in enumerate(sol):
                if v-(size-i) == c or v+(size-i) == c:
                    check = False
                    break

            if check:
                temp = sol[:]
                temp.append(c)
                queen_check(temp, size+1)

    queen_check([], 0)

    return cnt
