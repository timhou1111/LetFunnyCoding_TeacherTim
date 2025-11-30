# 函式function  --> 功能（剪刀）/函數f(x)
# 函式代表"可重複利用"的程式
# 函式也可以理解成，建立一座工廠，把輸入進去的東西，做相同的加工。

# def -->建立函式名字叫做abc
#()-->代表是你要處理的變數-->原料（工廠要處理的）
def abc (a, b):
    ans = a+b #工廠進行加工
    return ans #把結果還給顧客

# print(abc(10,40))

# print(abc(888,888))

temp = abc(1,1)

# print(temp)

#=======練習題=========
#建立出一個(7x+6y)*z-p --> 練習題
def function_caculator (x,y,z,p):
    return((7*x+6*y)*z-p)

# print("function_caculator輸出",function_caculator(1,2,2,2))


# function可以不要retrun
# function 可不可以不要return, 如果不要retrun, 就變成廣播電台
# def love_boardcast (name):
#     print("我喜歡你"+name)


# love_boardcast("雅音")


#BMI作為一參考:
def bmi_caculator7788(w,h):
    w = float(w)
    h = float(h)
    bmi = w / (h ** 2)
    return bmi




# ====APCS考試=====
# APCS --> 重要，但是不會建立函式也可以解題目。
# 選擇題，每一個題目都是函式


# https://zerojudge.tw/
