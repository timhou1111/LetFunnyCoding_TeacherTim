# https://zerojudge.tw/ShowProblem?problemid=f312

# 小筆記：
# x = -float('inf') -->表示負無限大。如果float('inf')就代表正無限大
# 自己設定數字可能會遇到產值（本題函式輸出數字）比max_total還要小，導致直接輸出max total
data1 = input().split()
a1 = int(data1[0])
b1 = int(data1[1])
c1 = int(data1[2])

data2 = input().split()
a2 = int(data2[0])
b2 = int(data2[1])
c2 = int(data2[2])

n = int(input())

max_total = -float('inf')


for x1 in range(n + 1):

    x2 = n - x1

    y1 = a1 * (x1 * x1) + b1 * x1 + c1

    y2 = a2 * (x2 * x2) + b2 * x2 + c2

    current_sum = y1 + y2

    if current_sum > max_total:
        max_total = current_sum  

print(max_total)

