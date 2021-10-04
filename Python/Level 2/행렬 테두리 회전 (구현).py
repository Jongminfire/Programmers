def rotate(x1, y1, x2, y2, matrix):
    temp = matrix[x1][y1]
    min_value = temp
    
    for x in range(x1, x2):
        matrix[x][y1] = matrix[x + 1][y1]
        min_value = min(min_value, matrix[x][y1])

    for y in range(y1, y2):
        matrix[x2][y] = matrix[x2][y + 1]
        min_value = min(min_value, matrix[x2][y])
    
    for x in range(x2,x1,-1):
        matrix[x][y2] = matrix[x-1][y2]
        min_value = min(min_value, matrix[x][y2])
    
    for y in range(y2, y1,-1):
        matrix[x1][y] = matrix[x1][y - 1]
        min_value = min(min_value, matrix[x1][y])

    matrix[x1][y1+1] = temp
    
    return min_value


def solution(rows, columns, queries):
    matrix = []
    answer = []

    for i in range(rows):
        temp = [v + 1 for v in range(i * columns, i * columns + columns)]
        matrix.append(temp)

    for x1, y1, x2, y2 in queries:
        min_value = rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix)
        answer.append(min_value)

    return answer