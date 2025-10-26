######陣列######


# 程式從上至下-->序列性（Sequence）
name_1 = "江國豪" #型態: 字串str()
speed_1 = 140 #型態: 數字int()
is_p_1 = True #型態: 布林

name_2 = "黃保羅"
speed_2 = 135
is_p_2 = True

name_3 = "詹智堯"
speed_3 = 120
is_p_3 = False



#######老闆要你三振他#########

# print("三振他，三振他",name_1)
# print("三振他，三振他",name_2)
# print("Hit抖 Hit抖",name_3)

# 通常，如果是『類似性質』，『相關性高』的資料。我們通常用陣列（串列，array,list）存放他
# 創造fubon_player的櫃子
# 從0開始，第0格"江國豪", 第1格"黃保羅",第2格"詹智堯"
fubon_player = ["江國豪", "黃保羅", "詹智堯", "曾峻岳", "王勝偉", "張育成"]
# print(fubon_player)
# print(fubon_player[1])


# 陣列可以存放各種型態
# 巧妙點：所有的第0項，都是江國豪的資訊
fubon_player = ["江國豪", "黃保羅", "詹智堯", "曾峻岳", "王勝偉", "張育成"] 
fubon_speed = [140, 135, 120]
fubon_is_picther = [True, True, False]

##也可以混合型態 （但是非常不建議，因為內容意義不明）
fubon_information = ["江國豪", 140, True, 18]

#如果沒有迴圈，所有『重複的事情』，都要一直手打
# print("三振他","三振他",fubon_player[0])
# print("三振他","三振他",fubon_player[1])
# print("三振他","三振他",fubon_player[2])
# print("三振他","三振他",fubon_player[3])
# print("三振他","三振他",fubon_player[4])
# print("三振他","三振他",fubon_player[5])


fubon_player = ["江國豪", "黃保羅", "詹智堯", "曾峻岳", "王勝偉", "張育成"] 
# i 在 fubon_player 輪流當每個值
# for i in fubon_player:
#     print("三振他","三振他", i)

# 用 range 去製造數字列，數字列可以製造出重複多次的效果，或是拿來做陣列的索引值（fubon_player[i]）。口訣：『頭一樣尾減1』
# range(5) --> 創造出 0~4
# range(99) --> 0~98
# range(1,10) --> 1~9
# range(3,55) --> 3~54
# range(44,57)--> 44~56

# i 在 range(5) 輪流當每個數字

#製造出重複多次的效果
# for i in range(8):
#     print("我愛你")

#拿來做陣列的索引值（fubon_player[i]）
fubon_player = ["江國豪", "黃保羅", "詹智堯"] 
fubon_speed = [140, 135, 120]
fubon_is_picther = [True, True, False]
for t in range(3):
    if fubon_is_picther[t] == True:
        print(fubon_player[t]+"是投手")
        print("三振他")
        print("球速"+str(fubon_speed[t]))


    
    
