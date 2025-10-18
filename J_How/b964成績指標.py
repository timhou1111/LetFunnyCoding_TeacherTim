x = int(input())
y= input()
y= [int(i) for i in y.split()]
print(' '.join(map(str,y)))
y = sorted(y)
for i in range (x):
    if y[0] >= 60:
        z = 0
    elif y[i] < 60:
        z = y [i]
if z == 0:
    print("best case")
else:
    print(z)
for i in range (x):
    if y[x-1] <= 60:
        z = 0
    elif y[i] > 60:
        z = y [i]
        break
if z == 0:
    print("worst case")
else:
    print(z)