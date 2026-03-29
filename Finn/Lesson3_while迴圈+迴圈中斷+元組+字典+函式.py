#==========迴圈===========
#while迴圈 --> 與for迴圈
#何時要用while迴圈？--> 當迴圈因為每個條件和需要停止的時候，就需要while

# height = 130 

# while height < 180:
#     print("喝牛奶")
#     height+=10
#     print("現在身高",height)

#思考 --> 以上程式有什麼問題 --> 無窮迴圈-->喝牛奶18863244 -->對電腦效能不好的
# 解決無窮迴圈? --> 【設立條件】並且【更動條件】

# 補充: 如何一開始就搞出無權迴圈 (筆試有可能會出現這個語法！！)
# c = 1
# while True:
#     print("我愛你",c)
#     c+=1



#for 可不可以取代 while --> 可以 --> 如何做? --> 用【break】來實踐

# 【筆試】break 是什麼意思? --> 把迴圈去打壞 --> 讓他不能運作 --> 中斷
# x = 0
# while x < 4: #滿足這個條件，我就往下做
#     print(" 『while範例』我愛你",x) #會印出4次我愛你，因為x會經歷0 1 2 3
#     x+=1


# for x in range(10):
#     #在這個for迴圈，我希望x>=4的時候，迴圈就不要做，跟上面的while一樣
#     if x >= 4:
#         break #跳離迴圈，老子不做了
#     print("『for範例』我愛你",x)


# 【筆試】Continue -->遇到Continue，就代表我直接【進入下一個回合】

# for i in range(10):
#     print("i現在是多少",i)
#     print("i%2是多少",i % 2 )
#     if i % 2 == 0:
#         continue
#     print(i)

    #這樣也可以
    # if i % 2 == 1:
    #     print(i)
    

#==========迴圈end===========

#以下這兩個是屬於array家族--> 
# x = []
# x.append(1)
# x.append(2)
# -->這個是array

#記得！！！ 取值的時候都跟陣列一樣使用方方括號[]（中括號）

# 元組 tuple --> 紀錄不可改變的事實 --> （array）
tuple_test = ("Monday", "Tuesday")
print(tuple_test[0])
# 如果你嘗試更改tuple裡面的值，程式會報錯
# tuple_test[0] = "MaModay"




# 字典 dictionary --> 鍵對值 對子 (資料庫)
#以 key 取出 value
#Hash map

       #key    value
dic = {"小明": 123456789,
       "小華": 998766543 
       }

name = ["小明", "小華"]
id = [123456789, 998766543]


#函式function

#function 就是指說 可以重複利用你寫過的東西，建立ＳＯＰ

# def function名稱  (參數1, 參數2......) :
#      function內容，其他程式，你要如何處理這些參數
#      return (可選，如果你的 function有計算結果，要用return還回去，只要印出文字，就不用return)


def test (a,b,c):
    ans = a+b+c
    if ans % 2 == 0:
        print("結果是偶數")
    else:
        print("結果是奇數")

print(test(5,7,7))