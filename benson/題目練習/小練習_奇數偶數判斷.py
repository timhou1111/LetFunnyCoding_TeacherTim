###複習-->輸入進來的型態(字串)
#x = input("請輸入你的東西") 


# 小練習: 讓使用者輸入一個數字，判斷他是奇數還是偶數。
# 奇說奇，偶說偶

###名稱: MOD --> %
# print(10%2) 5....0
# print(11%2) 5....1
# print(14%5) 2....4

# 重要提醒：APCS輸入，不要有提示字喔！！！
target_number = int(input("請輸入一個數字"))
if target_number % 2 == 0:
 print("偶")
else:
 print("奇")


