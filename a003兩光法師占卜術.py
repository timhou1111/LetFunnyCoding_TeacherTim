x = input()

md = x.split()

S=(int(md[0])*2+int(md[1]))%3
if S == 1:
    print("吉")
if S == 2:
    print("大吉")
if S == 0:
    print("普通")