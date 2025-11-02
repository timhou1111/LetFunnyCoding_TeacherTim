a = "abcd"
print(a[::-1])


x = input()
x = list (x)
yyy = []
if len(x)%2 == 1:
    odd = True
else:
    odd = False

if odd == True:
    w = int((len(x)-1)/2 +1)
    for i in range (1,w):
        yyy.append (x[i])
        
