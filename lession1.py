#數字
x = 6
y = 6.6

#字串
name = "Tim"
girl_friend = "vivi"
#布林值
r = True
x = False


print("my name is",name)

print(name+girl_friend)

print(name, girl_friend)




####轉換型態####
#str() -->轉換成字串
#int() -->轉換成變數

x = 6
y = 7
print(x+y)
print(str(x)+str(y))

x = "6"
y = "7"
print(x+y)
print(int(x)+int(y))


x = "6"
y = 7
# print(x+y) --> 會出錯，因為不同型態，不得相加。


###條件式###

x = 185
money = 120000
gay = False

# if else 條件式與布林（True, Ｆalse）高度相關。

#條件的起頭用if
if x > 180:
    print("i love you tim")
# 附加的條件用elif (else if)
elif money >= 100000:
    print("i love you tim")
# 如果都沒有滿足，用else做最後處理
else:
    print("byebye")



x = 185
money = 120000


#條件的起頭用if
if x > 180:
    print("i love you tim")
# 附加的條件用elif (else if)
    if money >= 100000:
        print("i love you tim")
# 如果都沒有滿足，用else做最後處理
else:
    print("byebye")
    

gay = True

# == 代表 如果左邊這個東西（數字，變數），是否與右邊的相等
if gay == True:
    print("(gay test)bye bye")

if gay == False:
    print("(gay test)i love you")


# if 後面到底判斷是什麼？
# Ans: 布林值，如果布林值返回“True"，就會進入條件式。如果是“False”就不回進入下方條件式。
#判斷式的本質會回傳true跟false

if True:
    print("我愛程式")

if False:
    print("我是甲")



# +-*/ -->他們是運算式，會計算數字
# >=< -->判斷式，會回傳true 跟 false
x = 185
print(x >= 1000)
print(x >= 150)



# != 不是
gay = True
print(gay != True)

# == 與 ＝ ，差異在哪
# = 賦值（重設）
# == 是判斷是否相等

x = 100
y = 100
print(y == 100)



###練習題###
# z  = input("請輸入你的數字") 
# print(type(z))


x= 100

print(type(x))

x = True
print(type(x))

x = "TIM"

print(type(x))



for i in range(50):
    print("我愛你", i)

x  =[1,2,3,4,5,6]
y = ["tim", "tom", "nina"]

print(x)
print(y)















