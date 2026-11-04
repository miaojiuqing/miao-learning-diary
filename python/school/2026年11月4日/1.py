height =  float(input("请输入您的身高:"))
weight = float (input("请输入您的体重:"))
BMI = weight/(height ** 2)
print (f"您的BIM值为{BMI}")
if BMI < 18.5:
    print("你偏瘦了")
elif BMI < 23.9:
    print("你正常了")
elif 24 < BMI < 27.9:
    print("你偏胖了")
elif BMI >= 28:
    print("你太胖了")