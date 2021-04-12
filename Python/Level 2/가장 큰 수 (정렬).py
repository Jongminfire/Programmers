def solution(numbers):
    answer = [str(i) for i in numbers]
    
    # 4자리수가 없을 경우 이전 숫자와 비교하기 위해서 x의 길이만큼 나눠줌
    answer.sort(key = lambda x : (x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]), reverse=True)

    # [0,0,0]의 경우 0이 나와야 하고 답은 str 형식이어야 하므로 str->int->str 형 변환
    return str(int(''.join(answer)))