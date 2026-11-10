'''
小 B 喜欢吃苹果。
她现在有 m(1≤m≤100)个苹果;
吃完一个苹果需要花费 t(0≤t≤100)分钟;
吃完一个后立刻开始吃下一个。
现在时间过去了 s(1≤s≤10000)分钟;
请问她还有几个完整的苹果？
'''
m = int(input("请输入要吃几个苹果(1-100):"))
t = int(input("你吃一个苹果要多长时间(分钟):"))
Apple_time = m * t
s = int(input("已经过了多少时间(分钟):"))
if (s > Apple_time):
    print(f"苹果已经吃完了,距离吃完已过了{s - Apple_time}分钟")
elif (s < Apple_time):
    APPLE_meichiwan = Apple_time - s #已经花费的时间
    APPLE_shengxia =  APPLE_meichiwan / t
    print(f"还剩{int(APPLE_shengxia)}个完整的苹果")