# 字典 - Dictionary
# 為什麼會需要字典-->查東西-->鍵對值-->對子

##沒有字典，資料就不會有，對子的概念
# lala = ["雅英", "朱垠", "粿粿"]
# phone = ["09123", "09456", "09789"]
# print(f"{lala[2]}的電話號碼是{phone[2]}")

##現在，需要要建立有『對子』概念的資料-->建立字典 (Key--Value) 字典(Key對Value)

phone_book = {"雅英": "09123",
              "朱垠": "09456",
              "粿粿": "09789"}


# 如何呼叫phone_book["粿粿"]

#第一個問題，value只能是字串嗎
lala_height = {"雅英": 168}
lala_loveme = {"雅英": True}
#第二個問題，key值可以不是字串嗎
will_lala_love_me = {180:True, 165:False}

#字典的鍵對值，可以是任意型態。

phone_book = {"雅英": "09123",
              "朱垠": "09456",
              "粿粿": "09789"}


#新增東西到字典
phone_book["夜寶地"] = "09888"

print(phone_book)

#遍歷字典
#items()-->取出key跟value
for key, val in  phone_book.items():
    print(f"{key}的電話是{val}")

#查字典的key
if "多慧" in phone_book:
    print("有多慧")

#查字典的value
if "090909" in phone_book.values():
    print("有090909")


######tuple元組#########
tuple_test = (1,2,3,4,5)
my_best_love = ("雅英", "多慧")

#取出tuple的值 --> 跟陣列完全一樣
print(my_best_love[1])

###宣告不出來的值，不可以以手動改變

x = ["雅英", "多慧"]
x[0] = "朱垠"
print(x)

my_best_love = ("雅英", "多慧")
my_best_love[0] = "朱垠" #取值跟陣列一樣
print(my_best_love)

#tuple --> 恆久不變的定律 

