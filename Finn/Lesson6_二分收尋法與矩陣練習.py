x = [1,2,3,5,7,8,19,42]

#為什麼要二分搜尋法？
# 陣列必須由小到大排列-->.sorted()
# 如果沒有二分搜尋法-->你就需要一個一個找，循序漸進，一個一個找。
# 我每一次都要排除一半的選項
# APCS --> 要找位置，且它是由小排到大，就要想到用二分搜尋法去找。

x = [1,2,3,4,5,6,7,8,9,10]

ans = 9

for i in range(len(x)):
    if x[i] == ans:
        print(ans,"找到了，是在第",i,"位置")



top = len(x)
down = 0
middle = 0. #用來抓出中間的數字

while top > down:
    middle = (top+down)//2

    if x[middle] == ans:
        print("找到了，位置在",middle)
        break
    elif x[middle] > ans:
        top = middle-1
    elif x[middle] < ans:
        down = middle+1


#==============矩陣================

#ACPS 
# 初級 --> 陣列
# 中級 --> 陣列 + 矩陣
# 中高級 --> 陣列 + 矩陣 + 資料結構
# 高級 --> 陣列 + 矩陣 + 資料結構 + 演算法

#遍歷內容
x = [
    [0,1,0,1,1,0],
    [1,1,1,0,0,0],
    [0,1,0,1,0,1],
    [0,1,0,1,0,0] 
    ]


count = 0
col = len(x)
row = len(x[0])


for i in range(col):
    for j in range(row):
        if x[i][j] == 1:
            count+=1

print(count)


for i in range(5):
    print(i)
    for j in range(3):
        print("我愛你",j)



#找特定的地方



#翻轉迴圈



     