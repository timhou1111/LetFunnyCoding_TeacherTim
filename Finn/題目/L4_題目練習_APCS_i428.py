# https://zerojudge.tw/ShowProblem?problemid=i428

#絕對值python語法為何？？？ --> abs(-99) 口訣：absolutely

n = int(input())

stations = []
for i in range(n):

    point = input().split()
    x = int(point[0])
    y = int(point[1])
    stations.append([x, y]) 

max_dist = -1        
min_dist =   float('inf')

for i in range(n - 1):

    x1 = stations[i][0]
    y1 = stations[i][1]
    
    x2 = stations[i+1][0]
    y2 = stations[i+1][1]
    
    dist = abs(x1 - x2) + abs(y1 - y2)
    
    if dist > max_dist:
        max_dist = dist

    if dist < min_dist:
        min_dist = dist

print(max_dist, min_dist)