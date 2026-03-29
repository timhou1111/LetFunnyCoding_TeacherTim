#APCS必備技能!!!!建構二維陣列
# 輸入一個 x 代表你輸入幾個陣列
# 接著輸入x個陣列
# 最後，把它組裝成二維陣列

# 例子: x 輸入3
# 接著我就可以輸入
#[1,2,3]
#[4,5,6]
#[88,99,00]

#最後把這三個一維陣列組裝成二維陣列
#輸出
#[
# [1,2,3],
# [4,5,6],
# [88,99,00]
#]

x = int(input("請輸入陣列的數量 x: "))
matrix = []

for i in range(x):
    row_input = input(f"請輸入第 {i+1} 個陣列的數字 : ")
    row = [int(num) for num in row_input.split()]
    matrix.append(row)

print("\n輸出結果：")
print("[")
for row in matrix:
    print(f"  {row},")
print("]")


#老師建議
print(matrix)

# x = input("請輸入陣列的數量 x: ")
# --> x = input()