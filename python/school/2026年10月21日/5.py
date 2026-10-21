a = float(input("请输入三角形的第一条边："))
b = float(input("请输入三角形的第二条边："))
c = float(input("请输入三角形的第三条边："))
d = a + b
e = a + c
f = b + c
if d > c and e > b and f > a:
    print("是个三角形") 
else:
    print("不是三角形")