# https://zerojudge.tw/ShowProblem?problemid=q836

k = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

p = 0 
v = k  

while v > 0:
    p = p + v 
    
    damage = 0
    if p % x1 == 0:
        damage += y1
    if p % x2 == 0:
        damage += y2
    
    v -= damage 
print(p)