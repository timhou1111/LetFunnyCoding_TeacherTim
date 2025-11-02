x = input()
x = list(x)

number = False
big = False 
small = False 
special = False
for i in x:
    if ((i). isdigit()):
        number = True
for i in x:
    if ((i). isupper()):
        big = True
for i in x:
    if (i.islower()):
        small = True


# little_a = ['a','b','c','d'...........]
# big_a = ["A", "B",......]
# in -->在家
# not in -->不在家
need_special = ["@","!","#"]

for i in x:
    if i in need_special:
        special = True


if number == False: 
    print("密碼不通 沒數字")
if big == False:
    print("密碼不通 沒大寫")
if small == False: 
    print("密碼不通 沒小寫")
if special == False:
    print("密碼不通 沒特殊符號")