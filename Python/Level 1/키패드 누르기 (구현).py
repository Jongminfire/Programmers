def solution(numbers, hand):
    answer = ''
    pad = [(),(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(2,4)]
    
    left = (1,4)
    right = (3,4)

    def change(i,direction,answer):
        if direction == left:
            answer += 'L'
        else:
            answer += 'R'

        return pad[i],answer
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left,answer = change(i,left,answer)
        elif i == 3 or i == 6 or i == 9:
            right,answer = change(i,right,answer)
        else:
            if i == 0:
                left_dist = abs(pad[10][0]-left[0])+abs(pad[10][1]-left[1])
                right_dist = abs(pad[10][0]-right[0])+abs(pad[10][1]-right[1])

                if left_dist < right_dist:
                    left,answer = change(10,left,answer)
                elif left_dist > right_dist:
                    right,answer = change(10,right,answer)
                else:
                    if hand == 'right':
                        right,answer = change(10,right,answer)
                    else:
                        left,answer = change(10,left,answer)
                
            else:
                left_dist = abs(pad[i][0]-left[0])+abs(pad[i][1]-left[1])
                right_dist = abs(pad[i][0]-right[0])+abs(pad[i][1]-right[1])

                if left_dist < right_dist:
                    left,answer = change(i,left,answer)
                elif left_dist > right_dist:
                    right,answer = change(i,right,answer)
                else:
                    if hand == 'right':
                        right,answer = change(i,right,answer)
                    else:
                        left,answer = change(i,left,answer)
            
    return answer