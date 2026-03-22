# 輸入一串數字，用空格分開。
# 40 50 70 80 90
# 幾個及格幾個不及格

#博丞
data = input("請輸入分數：")
scores = [int(s) for s in data.split()]

pass_count = 0
fail_count = 0

for s in scores:
    if s >= 60:
        pass_count += 1
    else:
        fail_count += 1

print(f"及格人數：{pass_count}")
print(f"不及格人數：{fail_count}")