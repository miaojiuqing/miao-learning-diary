age = int(input("请输入你的年龄："))
if age >=18:
    print("请进")
else:
    print("谁家小孩")

grade = float(input("你的考试成绩是多少："))
if grade >=60:
    print(f"{grade}分，意气风发啊")
if grade <=60:
    print(f"{grade}分，野狗一条啊")