#BMI機算機
#BMI過輕-->太瘦了（空格）老哥
#BMI過重-->該減肥了，過胖
#剛好--->剛好（空格）（空格）（空格）均衡老哥

weight = float(input("請輸入體重"))
hight = float(input("請輸入身高公尺"))
bmi = weight / (hight ** 2 )
if bmi < 18.5:
    print("太瘦了 老哥")
elif bmi > 24:
    print("該減肥了，過胖")
else:
    print("剛好   均衡老哥")


###小弟補充###