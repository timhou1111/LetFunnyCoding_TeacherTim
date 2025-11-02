###########複習###########
# x = input() #輸入進來的東西，一定是字串
# print(x)
# target = 123
# print(type(x)) #考場上忘記，就偷偷用這個語法看一下。

#印出來的語法
# print(x,x) #”,“就是用空個分離
#####新語法分享
#####假設ＡＰＣＳ考試要你印-->小華我愛你 or 小華（空格）我愛你 or 小華（空格）（空格）我愛你
#####小提醒：ＡＰＣＳ考試，打印出的內容，需跟題目完全一樣（要空格就給空格）
# print("小華 ",x)
# print(f"小華  {x}")

#陣列
# y = [1,2,3,4,5]
# print(y)
##利用索引值index來取出值
# print(y[2])

#迴圈
# for i in range(5):
#     print(i)

# for something_in_array in y:
#     print(something_in_array)
###########複習###########


print("###########延伸語法###########")
# APCS陣列自己輸入
#APCS考試時，要輸入一串東西給你做運算-->存成陣列
# all_grade = input()
# # 如何輸入？使用split()-->中文：撥開
# print(all_grade)

# all_grade = all_grade.split()
# print(all_grade)
# print(type(all_grade[2]))

#終極語法教學-->輸入進來的數字馬上就轉成數字，而非原本的字串
x = input() # -->1 2 3 (純文字)
test_score = [int(i) for i in x.split()]
# x.split() --> ["1","2","3"]
# i 輪流當字串 "1", "2" ,"3"
#一開始的[]，代表一個空的陣列
#int(i)，代表把每一個i，輪流換成int


print(test_score)
print(type(test_score[0]))






