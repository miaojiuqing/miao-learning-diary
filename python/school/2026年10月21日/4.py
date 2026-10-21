#练习1:输入圆的半径,计算圆的面积和周长
r = float(input("请输入半径: "))
area = 3.14159 * r * r
#面积S=nr2
circumference = 2 * 3.14159 * r # k C=2лr
print(f"面积： {area:.2f}")
print(f"周长：{circumference: .2f}")

# 练习2：华氏温度转摄氏温度
f = float(input("华氏温度: "))
c = (f - 32) / 1.8
print(f"摄氏温度： {c:.1f}")