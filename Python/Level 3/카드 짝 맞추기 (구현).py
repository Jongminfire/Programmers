from collections import defaultdict,deque
from itertools import permutations
import copy

def findMatrix(sx,sy,graph,ex,ey):
  visited = [[-1 for _ in range(4)] for _ in range(4)]
  visited[sx][sy] = 0
  dq = deque()
  dq.append((sx,sy))

  while dq:
    x,y = dq.popleft()

    if x == ex and y == ey:
      return visited[ex][ey] + 1

    for i in range(4):
      if 0 <= x+i < 4:
        if visited[x+i][y] == -1 and (graph[x+i][y] != 0 or x+i == 0 or x+i ==3):
          dq.append((x+i,y))
          visited[x+i][y] = visited[x][y] +1
          break

    for i in range(4):
      if 0 <= x-i < 4:
        if visited[x-i][y] == -1 and (graph[x-i][y] != 0 or x-i == 0 or x-i == 3):
          dq.append((x-i,y))
          visited[x-i][y] = visited[x][y] +1
          break

    for i in range(4):
      if 0 <= y+i < 4:
        if visited[x][y+i] == -1 and (graph[x][y+i] != 0 or y+i == 0 or y+i == 3):
          dq.append((x,y+i))
          visited[x][y+i] = visited[x][y] +1
          break

    for i in range(4):
      if 0 <= y-i < 4:
        if visited[x][y-i] == -1 and (graph[x][y-i] != 0 or y-i == 0 or y-i ==3):
          dq.append((x,y-i))
          visited[x][y-i] = visited[x][y] +1
          break
    
    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
      if 0 <= nx < 4 and 0 <= ny < 4:
        if visited[nx][ny] == -1:
          dq.append((nx,ny))
          visited[nx][ny] = visited[x][y] + 1

  return visited[ex][ey]+1

def solution(board, r, c):
    answer = int(1e9)
    dic = defaultdict(list)
    left = set()
    now = (r,c)

    for y in range(4):
      for x in range(4):
        if board[x][y] != 0:
          dic[board[x][y]].append((x,y))
          left.add(board[x][y])

    for lst in permutations([i for i in left],len(left)):
      temp = 0
      tempMatrix = copy.deepcopy(board)
      now = (r,c)

      for n in lst:
        x1,y1 = dic[n][0]
        x2,y2 = dic[n][1]
        dist1 = findMatrix(now[0],now[1],tempMatrix,x1,y1)
        dist2 = findMatrix(now[0],now[1],tempMatrix,x2,y2)

        if dist1 < dist2:
          temp += dist1
          tempMatrix[x1][y1] = 0
          temp += findMatrix(x1,y1,tempMatrix,x2,y2)
          now = (x2,y2)
        else:
          temp += dist2
          tempMatrix[x2][y2] = 0
          temp += findMatrix(x2,y2,tempMatrix,x1,y1)
          now = (x1,y1)
        
        tempMatrix[now[0]][now[1]] = 0

      answer = min(temp,answer)

    return answer


# solution([[0, 0, 1, 0], [1, 0, 0, 0], [4, 4, 3, 2], [0, 3, 2, 0]],2,0) 반례 (답:18)