def solution(files):
    file = []
    answer = []
    for i, v in enumerate(files):
        head_index = 0
        number_index = len(v)

        for hi, hv in enumerate(v):
            if hv.isdigit():
                head_index = hi
                break

        for j in range(head_index, len(v)):
            if not v[j].isdigit():
                number_index = j
                break

        # 대소문자 구별하지 않으므로 lower로 처리
        file.append((v[:head_index].lower(), v[head_index:number_index], i))

    file.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))

    for i in file:
        answer.append(files[i[2]])

    return answer
