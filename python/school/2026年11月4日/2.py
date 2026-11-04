money = float(input("您的购物金额是:"))
if money < 100:
    print("不打折")
elif 100 <= money <500:
    money = money * 0.9
    print("打九折")
elif 500 <= money <1000:
    money = money * 0.8
    print("打八折")
elif 1000 <= money:
    money = money * 0.7
    print("打七折")
print(f"您的应付金额为 :{money}元")