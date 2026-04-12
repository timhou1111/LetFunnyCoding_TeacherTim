# https://zerojudge.tw/ShowProblem?problemid=a005
t = int(input())

for i in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    d = int(line[3])
    
    if (b - a) == (c - b):    
        diff = b - a
        e = d + diff
    else:        
        ratio = b // a
        e = d * ratio
        
    print(a, b, c, d, e)