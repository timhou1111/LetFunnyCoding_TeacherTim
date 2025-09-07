# 蛇行命名
emp_name = "tim"
boss_name = "syc"

#駝峰命名
EmpName= "tim"
BossName = "syc"
MySalary = 72000
BossSalary = 90000

#變數 type(number)
number = 2  # str()
word = "tim" #輸入一律都是字串 int() 
truth = False

print(type(number))

#條件式
x = 10
if x >= 10:
    print("好大")
elif x >=20:
    print("更大")
else:
    print("好小")


# 陣列（array, list）, for loop, dictionary, tuple

score1 = 100
score2 = 135
score3 = 85

if score1 > score2 and score1 > score3:
    print("最高分是", score1)
elif score2 > score1 and score2 > score3:
    print("最高分是", score2)
else:
    print("最高分是", score3)


everybody_score = [100, 135, 80, 90]

print(everybody_score)
print(max(everybody_score))
print(min(everybody_score))
everybody_score.append(200)
print(everybody_score)

everybody_score.pop()
print(everybody_score)

everybody_score.remove(80)
print(everybody_score)

everybody_score.insert(0,300)
print(everybody_score)

#必記！！！程式是從0開始
print(everybody_score[0],everybody_score[1])
print(str(everybody_score[0])+str(everybody_score[1]))

# list 可以有各種不一樣的資料型態
family = ["tim", "tom", "tommy"]
print(family)
truth = [True,False,True]
print(truth)

#告訴你，但不建議
person = ["tim", 180, False]
print(person)

#如何修改list的值
family = ["tim", "tom", "tommy"]
family[0] = "timmy"
print(family)



#list-->[]
#index從0開始，太極從0開始
#真實世界-->存放類似的資料


# 導入時間套件，別人寫好的套件
import time

family = ["tim", "tom", "tommy","melody"]
print("歡迎光臨", "tim")
print("歡迎光臨", "tom")
print("歡迎光臨", "tommy")
print("歡迎光臨", "melody")
print("善用array")
print("歡迎光臨", family[0])
print("歡迎光臨", family[1])
print("歡迎光臨", family[3])

#迴圈 loop, for loop
print("歡迎光臨")

#迴圈讓我們不用重複的做一樣的Code。
print("快使用迴圈")

# python 迴圈的真理！！！！！！
# 宣告i變數，i輪流當in後面的東東。
# in 後面可以是range, 也可是陣列
print(range(5)) #--> 0~5
for i in range(5):
    print(i)

family = ["tim", "tom", "tommy","melody"]
for j in family:
    print(j)

# len的功能-->幫助你去遍歷所有的陣列內容
family = ["tim", "tom", "tommy","melody"]
print(len(family))# -->會印出這個陣列的長度 所以是4
# 善用range做組合
print(range(len(family)))# 就等於range(5)
# len 就是可以自動感應陣列裡面的值。


# x = input("新來的家庭成員")
family = ["tim", "tom", "tommy","melody", "vic", "lisa", "yoyo", "bob"]
family.append(x)
print(len(family))
for i in range(len(family)):
    print(family[i])

#range(5)-->生出0~4
#如果我今天要1~4怎辦
#range(1,5)


#for 中 for
for i in range(3):
    for j in range(4):
        print("你好")
    

# while (如果)
# 有滿足，就繼續往下做。
# 小心無窮迴圈
x = 0

while x<=5:
    print("我愛你")
    print("x now is", x)
    x+=1

# 計算出1~11的質數
for i in range(1,11):
    can_be_devide_count = 0
    for j in range(1,i+1):
        if i % j == 0:
            can_be_devide_count+=1
    if can_be_devide_count == 2:
        print("你是質數",i)


for i in range(1,1000):
    if i %2 == 0:
        print(i)


#輸入東西存到陣列
#連續輸入一串東西，把它轉成陣列
#請用split()-->用遇到空白做切割，塞到陣列
#請用split("＠")-->用遇到@做切割，塞到陣列

x = input("連續輸入數字")
print("split()之前", x)
x = x.split()
print("split()之後", x)

total = 0
for i in range(1,len(x)+1):
    total+=int(i)
print(total)

#dic, tuple
#矩陣，二維
#物件