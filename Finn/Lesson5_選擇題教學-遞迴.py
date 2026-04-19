#為什麼要理解遞迴-->因為APCS很愛考！
#遞迴的優點 --> 減少程式碼的行數
#遞迴缺點 -->易讀性不好


#理解遞迴之前，先理解函式

# 沒有的return的函式，通常是拿來印出資訊，不會返回任何值。
# 沒有return --> 沒有辦法使用在遞迴
def hello(name):
    print('我愛你', name)

hello("李珠恩")

# 有retrun，代表會返會值
# ！！重要:為什麼有return要print，但是沒有retrun不用
# --> return 的本質，就是返回一個數字給你～！
def add (num1, num2):
    return num1 + num2

print(add(10,20))


#APCS愛考三大題型：
# 給你迴圈慢慢看
# 大腸包小腸
# 遞迴


#補充：APCS選擇題愛考的～！function裡面包function

def fun1 (num1,num2):
    return num1*num2

def fun2 (c,d):
    return fun1(4,5)+c+d

print(fun2(3,2)) # -->25，因為fun2執行時他發現裡面有fun1，所以會先將fun(4,5)計算完畢後，得到20，再回來加上3跟2。


#遞迴的定義：function裡面有function。且function名稱相同(自己呼叫自己)
# 題目使用者輸入一個正整數字n，回傳1+2+3.....n的總和。

#一般版；
# n = int(input())
# toto = 0

# for i in range(1,n+1):
#     toto += i

# print(toto)

# 遞迴
def add_all (n):
    if n == 1: #退出點
        return 1
    else: 
        return n + add_all(n-1)

# 看看這個遞迴（經典的）：
def f_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return f_num(n-1) + f_num(n-2)


# 找最大公因數的遞迴（APCS一定會考，而且超愛）
    

    












    
