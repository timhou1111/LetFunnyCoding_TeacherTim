# 英文 --> 每次都一有一張全班的成績單
#算平均值
#不及格人數
#範例輸出
# 全班人數10人
# 平均80分
# 不及格7人
# 班上最高分 -->
x = input()
ans_score = [int(i)for i in x.split()]
average = sum(ans_score) / len(ans_score)
print(average)
fail = 0
the_best = -1
for score in ans_score:
    #用來判斷不及格人數
    if score < 60:
     fail += 1
    #用來判斷最高分
    if score > the_best:
       the_best = score

print(f"不及格人數 {fail}")
print(f"班上最高分 {the_best}")

print(max(ans_score))
print(min(ans_score))



