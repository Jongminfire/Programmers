from itertools import permutations


# a,b의 이름 검사
def name_check(a, b):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if b[i] == '*':
            continue
        elif a[i] != b[i]:
            return False

    return True


def solution(user_id, banned_id):
    ans = []

    # user_id의 순서에 따라 바뀔 수 있으므로 combination 대신 permutation 사용
    for users in list(permutations(user_id, len(banned_id))):
        check = True

        # 이름이 다를 경우 check = False
        for i in range(len(users)):
            if not name_check(users[i], banned_id[i]):
                check = False
                break

        if check:
            users = set(users)  # users의 중복을 막기 위해서 set로 순서를 없앤 뒤 ans에 삽입
            if users not in ans:
                ans.append(users)

    return len(ans)
