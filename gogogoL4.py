# 函式-->function
# 1. 縮減重複的程式
# 2. 薪火相傳-->你寫好的程式給別人用

# 如果沒有函式(function)

# score1 = int(input())

# if score1 >= 90:
#     grade1 = "A"
# elif score1 >= 80:
#     grade1 = "B"
# elif score1 >= 70:
#     grade1 = "C"
# else:
#     grade1 = "D"
# print(f"學生1: {grade1}")

# 如果你有200的地方需要用到分數計算，你就會需要200處一模一樣的程式碼

def score_cacu(score):
    if score >= 90:
        grade1 = "A"
    elif score >= 80:
        grade1 = "B"
    elif score >= 70:
        grade1 = "C"
    else:
        grade1 = "D"
    print(f"學生: {grade1}")



# 如果，你想要你的工廠（function）回傳數字，文字，true/flase給你
# 要使用return, 否則print只會單純在螢幕上做顯示

def cacu_bmi(height, weight):
    height_meter = height/100
    bmi = weight/(height_meter*height_meter)
    return bmi


# 假設『你需要對function的結果做計算，怎麼辦？』用return。把值丟回去給你
#bmi2.0 --> bmi + 20
x = cacu_bmi(180, 70) + 20
print(x)

    


def odd(num):
    if num%2 == 1:
        return True
    elif num%2 == 0:
        return False
    

y = odd(2001)

print(y)