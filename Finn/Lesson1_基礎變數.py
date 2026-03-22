# print("我愛你") #字串
# print(520)  #數字
# print(True) #布林值

# APCS 是怎麼判斷答案的？ 他是看你print的結果來決定你的答案是否正確。
# 我愛你520
# 我愛你 520
#!!!輸出格式一定要跟範例一樣，標點符號不可漏。

#逗點-->代表空白
# print("我愛你","520")

#對or錯
#print("我愛你"+520) 錯，！！！數字跟字串是不能做數學運算
#緊密相連-->用＋    有空白-->逗號
# print("我愛你"+"520")
# print("我愛你 520")


#變數
# x = 520     #數字
# y = "我愛你" #字串
# z = True    #布林值

# print(x)
# print(y)
# yy = "阿美"
# print(y + yy)

# 專家思維_變數的命名_有意義（變數多，好辨認）
# myName      #駱駝駝峰
# my_name     #蛇型
# personILove 
# person_i_love  


#變數難道只能自己一直宣告嗎？
# 輸入-->讓只用者輸入一段東西，存起來。

#============APCS統一用這個Start========
# x = input() 
#============APCS統一用這個End========

# input進來的任何的東西，全部都是『字串』
# x = int(input())
# print(5+int(x))
# str(x) --> 轉回字串


#if (條件)
tall = 185
weight = 90
salary = 200000000

# APCS考試，發現輸出怪怪的，優先檢查if else
# if 是一個獨立的條件串，elif 是他的附屬條件，每一個條件串，都只會進到一個結果

if tall > 180:
    print("交往")

if weight > 80:
    print("交往")

if salary > 3000000:
    print("交往")
else:
    print("7414")
















