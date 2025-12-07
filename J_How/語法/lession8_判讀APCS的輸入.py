# APCS

#現在連續輸入法，已經不太考了

# 注意空格 --> x.split() 『[int(i) for i in x]』/ list(x)
# 注意換行 -->使用者按了Enter，你就要接住這個變數

# year_1 = input()
# year_2 = input()

# APCS --> 二維陣列
# x = [
#     [1,2,3],
#     [4,5,6]
# ]

# test = []
# c = [1,2,3]
# b = [4,5,6]

# test.append(c)
# test.append(b)

# test_2 = []
# y = 123
# p = 456

# test_2.append(y)
# test_2.append(p)

# print(test_2)



# 輸入
# 2
# [
# [1,3,4],
# [4,6,7]
# ] 

# 輸入
# 3
# [
# [1,3,4],
# [4,6,7],
# [7,8,9]
# ] 

# 輸入
# 4
# [
# [1,3,4],
# [4,6,7],
# [7,8,9],
# [6,6,6]
# ] 

# 輸入二維陣列有幾個值
level = int(input())
matrix = []
for i in range(level):
    temp = input().split()
    temp = [int(j) for j in temp] #[int(i) for i in x]
    print(temp)
    matrix.append(temp)

print(matrix)
    




