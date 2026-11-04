import random
ji_fen = 0
ren_fen = 0
options = ["石头","剪刀","布"]
quan = input(str("你出'石头'还是'布'还是'剪刀'："))
print (f"你选择了{quan}")
ji_quan = random.choice(options)
print (f"电脑出了{ji_quan}")

if ji_quan == "石头" and quan == "剪刀":
    print ("You lose!")
    ji_fen = +1
if ji_quan == "剪刀" and quan == "石头":
    print ("You Win!")
    ren_fen = +1

elif ji_quan == "布" and quan == "石头":
    print ("You lose!")
    ji_fen = +1
elif ji_quan == "石头" and quan == "布":
    print ("You Win!")
    ren_fen = +1

elif ji_quan == "剪刀" and quan == "布":
    print ("You lose!")
    ji_fen = +1
elif ji_quan == "布" and quan == "剪刀":
    print ("You Win!")
    ren_fen = +1

elif ji_quan == quan:
    print ("是平局哦")
else :
    print("你做了错误的选择")