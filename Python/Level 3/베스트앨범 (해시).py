def solution(genres, plays):
    total = {}
    count = {}
    answer = []
    
    for i in range(len(genres)):
        if genres[i] not in total:
            total[genres[i]] = plays[i]
            count[genres[i]] = [(plays[i],i)]
        else:
            total[genres[i]] += plays[i]
            count[genres[i]].append((plays[i],i))

    for genre in sorted(total.items(), key=lambda x:x[1], reverse = True):          # total이 큰 순으로 정렬
        lst = sorted(count[genre[0]], key=lambda x:(-x[0],x[1]))                    # genre의 재생 횟수로 정렬 후 고유 번호가 작은 순서대로 정렬
        
        answer.append(lst[0][1])
        
        if len(lst) > 1:                                                            # 장르의 노래가 1개 이상이면 2개까지 추가
            answer.append(lst[1][1])

    return answer