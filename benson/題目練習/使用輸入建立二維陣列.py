# 製作出一個輸入 
# 
# 第一個數字-->班上有幾個人-->這個二維陣列有幾層
# 使用者輸入分數-->國英數-->100(空)80(空)66(Enter) -->第一個人的分數


##當有換行，代表使用者按了Enter
# 3
# 100 100 100
# 99 99 99
# 88 88 88

# -->我要得到
# [
#     [100,100,100],
#     [99,99,99],
#     [88,88,88]
# ]

# 當我們按下Enter的時候，input才會抓住這個值
# input 要按下 enter, 抓到值之後，才會繼續往下跑
people_num = int(input()) 
print("people_num 的 值", people_num)
people_score = []

for i in range(people_num): #假設我people_num輸入5，這個迴圈迴圈會跑5次
    this_people_score = input() #使用者輸入這個人的分數 100 77 88
    print("這回合input", this_people_score)
    this_people_score = [int(i) for i in this_people_score.split()] #切分，形成陣列 ["100", "77", "88"]
    print("切分split之後", this_people_score)
    people_score.append(this_people_score)
    print("加入全班分數people_score", people_score)

print(people_score)
    
    
