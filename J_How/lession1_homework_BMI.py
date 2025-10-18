print("test")

name = input("請輸入姓名: ")
height = int(input("請輸入身高"))
weight = int(input("請輸入體重"))

print("測試資料型態")
print(type(height))
print(type(weight))

# 計算BMI
height_m = height / 100  # 轉成公尺
bmi = weight / (height_m * height_m)

# 判斷健康狀況
print(f"\n{name}的BMI是: {bmi:.2f}")

if bmi < 18.5:
    print("太瘦了 老哥")
elif bmi <= 24.9:
    print("正常範圍")
elif bmi <= 29.9:
    print("體重過重")
else:
    print("該減肥了，過胖")
