#演算法

#演算法與資料結構

#資料結構 --> 我如何設計，我如何構想，我如何有效率的存取資料。
#方案一
# x = ["小明", "小華"]
# sex_intention =["gay", "None_gay"]
#方案二
# sex_dic = {"小明":True,  "小華": False}

#演算法 --> 完成一個任務，算法的步驟


#####排序法#####
###小--->大###
# 三方交換
target_1 = 6
target_2 = 9

temp = target_1
target_1 = target_2
target_2 = temp

#python 三方交換
target_1, target_2 = target_2, target_1

#氣泡排序法-->越大的泡泡，往右浮
x = [64, 43, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

bubble_sort(x)
print(x)




#選擇排序法
x = [64, 43, 25, 12, 22, 11, 90]



def select_sort(arr):
    for i in range(len(arr)):
        this_round_small = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[this_round_small]:
                this_round_small = j
        arr[i] , arr[this_round_small] = arr[this_round_small], arr[i]

    return arr

select_sort(x)




x = [1, 43, 25, 12]
for i in range(len(x)-1):
    thisroundsmall = x[i]
    for j in range (i+1,len(x)-1):
        if x[j]> x[j+1]:
            thisroundsmall = x[j+1]
    if x[i]> thisroundsmall:
        x[i],thisroundsmall= thisroundsmall,x[i]
print(x)




most_small = 3

ee = [1,2,3]

ee[1], most_small = most_small , ee[1]

print(ee)
print(most_small)



