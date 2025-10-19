######條件式#####

######判斷式#####

######判斷式的結果#####
x = True
y = False
#######補充: 如果一次要宣告兩個變數#####
a , b = True, False


######如何產生條件式#####
#######!!!!使用運算子--> >, <, >=, ==, <=, !=#####

######gay 喜歡我 （嚇死）#####

# print(height > 180)
# print(height < 170)
# print(height == 176)
# print(height != 176)


######純粹比較字，純粹比較字有沒有一樣#####
#print(type == "霸道總裁")

gay = False

#print(gay == False)

##### = 跟 == 差在哪 #####

### 把5存到x （x 存放 5） ##
#x = 5
### x 也沒有等於5 ###
#x == 5



##########if（如果） elif（追加條件） else(否則) #############

# 我的條件（大砲哥）
height = 175
money = 700000
handsome = 99


# if elis 代表控制程式碼要不要執行，如果判斷式是『true』才要做，如果是『false』就不會做
# elif （else if） 代表 if 後面追加的條件
# and or

# 雅音的條件
if height > 188 and handsome > 95:
    print("雅音超愛")
elif handsome > 95:
    print("暈船了")
elif money > 150000:
    print("抖內金主")
else:
    print("路人甲")    


#朱垠
# 棒球手 或者 帥歐巴 --> 有點心動
# 月收入 小於 200000 --> 看不上
# 是棒球手帥歐巴 同時 月收入超過50W
# 其他人 -->  普通觀眾
# 條件要讓我用輸入的



# 輸入進來的東東，一律受字串型態，數字運算，轉型態。
yyy = int(input())

print(type(yyy))

cccc = str(10000)

print(type(cccc))






