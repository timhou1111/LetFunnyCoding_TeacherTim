# https://zerojudge.tw/ShowProblem?problemid=g275

#要輸入幾句
input_num = int(input())

for i in range(input_num):
    # 讀取兩句對聯
    line1 = input().split()
    line2 = input().split()

    violation = "" 

    #A: 二四不同二六同：每一句第二、四個字必須不同平仄，而第二、六個字必須相同平仄
    if (line1[1] == line1[3] or line1[1] != line1[5]) or (line2[1] == line2[3] or line2[1] != line2[5]):
        violation = violation + "A"
    
    #B: 仄起平收：第一句的結尾必須為仄聲，第二句的結尾必須為平聲
    if line1[6] == "0" or line2[6] == "1":
        violation = violation + "B"
    
    # C: 上下相對：第一、二句的第二、四、六個字平仄必須不同
    if line1[1] == line2[1] or line1[3] == line2[3] or line1[5] == line2[5]:
        violation = violation + "C"

    if violation == "":
        print("None")
    else:
        print(violation)
