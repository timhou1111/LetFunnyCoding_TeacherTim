# https://zerojudge.tw/ShowProblem?problemid=m931

#你要輸入幾個角色
rule = input()
x = []
power = []
y = 0
for i in range (int(rule)):
    z = input()
    z = z.split()
    x.append(z)    
    power.append(int(z[0])** 2 +int(z[1])** 2)

power1 = power.copy()
power1.sort()
y = (power.index(power1[-2]))
print (" ".join(x[y]))

