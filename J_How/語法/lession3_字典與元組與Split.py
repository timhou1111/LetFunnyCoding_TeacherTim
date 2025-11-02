# Dictionary 字典

# 如果沒有ｄｉｃｔｉｏｎａｒｙ
student = ["王大明", 16, 180, True]

if student[2] >= 180:
    print("邀請加他入籃球隊")
if student[3] == True:
    print("介紹男體育老師給他")

# 程式太長, 型別混雜。
# 誰知道16跟180是什麼意思
# 無法分別資料型態
# --> 字典 key-->value

student_d = {"姓名": "王大名", 
             "年紀": 16, 
             "身高": 180, 
             "是不是蓋": True
             }

#取值 字典名稱[key]
print(student_d["是不是蓋"])
print(student_d["姓名"])


if student_d["身高"] >= 180:
    print("邀請加他入籃球隊")
if student_d["是不是蓋"] == True:
    print("介紹男體育老師給他")

#改值
student_d["是不是蓋"] = False
print(student_d)
    
print("################練習時間####################")
# x = input("輸入你的姓名, 電話, 興趣，要用空格隔開喔")

# x = x.split()

# print(x)

# dic = {}

# dic["姓名"] = x[0]
# dic["電話"] = x[1]
# dic["興趣"] = x[2]

# print(dic)

print("####################################")
#tuple
# 跟陣列是完全一樣的
#如何宣告tuple
ttt = ("F133333333", "男")
lis = ["F133333333", "男"]

# 這個是世界上，有很多不變的真理！！ --> tuple
# 例如：我的身份證


x = input("請輸入日期")

md = x.split()

S=(md[0]*2+md[1])%3
if S == 1:
    print("吉")
if S == 2:
    print("大吉")
if S == 0:
    print("普通")



