# https://zerojudge.tw/ShowProblem?problemid=a003

input_data = input().split()
M = int(input_data[0])
D = int(input_data[1])

S = (M * 2 + D) % 3

if S == 0:
    print("普通")
elif S == 1:
    print("吉")
else:
    print("大吉")