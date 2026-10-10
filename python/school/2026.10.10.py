# 项目一：个人简历
name = "淼清"
gender = "沃尔玛购物袋"
age = 20
height = 177.7
weight = 80.5
school = "本科院校"
institute = "智能工程学院"
major = "人工智能"
hobby = "写游戏脚本、看脚本打游戏"
personal_website = "https://4kkxskd2z19hm.aiforce.cloud/app/app_17a45dkksja"
survival_status = True
print("\n ===个人简历=== \n")
print (f"姓名：{name} \n 性别：{gender} \n 年龄：{age}")
print (f" 身高：{height}cm \n 体重：{weight}kg")
print (f"学校：{school}  \n 学院：{institute} \n 专业：{major}")
print (f"个人爱好：{hobby}")
print (f"个人网站：{personal_website}")
print (f"活着吗：{'是' if survival_status else '否'}")

print("\n \n\ \n \n \n \n \n ")

# 项目二：天天向上的力量
import math
# day_up = 0.01
days = 356
day_up = float(input("每天进度多少（如0.01代表1%）："))
# 每天进步百分之多少，一年后会咋样
result_up = (1 + day_up) ** days
print(f"每天进步{day_up * 100:.0f}%,一年后：{result_up:.2f}倍")

print("\n \n\ \n \n \n \n \n ")
# 项目三：进度条
import time

print("==== 执行开始 ====")

for i in range(11):
    percent = i * 10
    #percent 通常译为“百分之……”
    # 也可表示“百分比”，指每一百份中所占的数量或比例
    filled = "*" * i
    # filled 是 fill 的过去式和过去分词
    # 也常作形容词，主要表示已经填满、装满、充满，或填写完成
    empty = "." * (10 - i)
    # empty 常见作形容词，意为“空的、空无一物的”；
    # 作动词时意为“倒空、清空”。它的核心含义是里面没有东西，或把容器、空间等变得没有东西
    print(f"{percent:3d}%[{filled}->{empty}]")
    time.sleep(0.3)#每行延迟0.3秒假装真的在加载

print("==== 执行结束 ====")
