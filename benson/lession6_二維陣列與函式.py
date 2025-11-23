# APCS考試
## 選擇 --> giving code and get result
## 實作 --> 中級可挑戰，（下一階）中級採得穩，踏上中高

# 複習 ＊＊＊三星
dic = {"小明": 180, "小華":166}
# 陣列，字典，元組-->取值都是用方方括號
#print(dic["小明"])
dic["暖暖"]=190
#print(dic)

#元組
tup = {1,2,3,4}
#print(tup)


##二維陣列

x = [1,2,3,4,5] #陣列-->一維陣列

#學校成績系統
# [國文, 數學, 英文]
# 陣列 --> 櫃子（相似的資料）
benson = [96, 101, 97]
sam = [60, 50, 66]
lisa = [79, 55, 88]

# 班上有多少人？41人
# 就必須要創造出41個陣列，且每個陣列不同-->複雜＋不好算

# 二維陣列
# 相似的資料，聚合再聚合

# [國文, 數學, 英文, 化學, 物理]
everybody_score = [
    [96, 101, 97, 100, 107],
    [60, 50, 66, 57, 89],
    [79, 55, 88, 45, 66],
]

#他也可以是字串
# 住飯店 --> 先找樓層再找房間
everybody_name = [
    ["小明","大華", "大大"], #第0樓
    ["嗨嗨", "成成", "積積",], #第1樓.  
    ["明明","中漢", "大明"], #第2樓
]

print(everybody_score)

# 取出一個人的分數
print(everybody_score[0])
print(everybody_score[1])
#算出benson(二維陣列裡面的第一人)的成績總和
print(sum(everybody_score[0]))
#取出第二個人sam的最低分數(min), 最高分數(max)
print(min(everybody_score[1]))

#如何取出單一個數值
# 住飯店 --> 先找樓層再找房間
print(everybody_name[1][2])

# 如何建立二維陣列，用陣列
test = []
inside_1 = [1,1,1]
inside_2 = [2,2,2]
inside_3 = [3,3,3]

test.append(inside_1)
test.append(inside_2)
test.append(inside_3)

print(test)






