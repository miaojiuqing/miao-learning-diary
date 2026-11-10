m, t, s = map(int, input().split())
Apple_time = m * t
if (s > Apple_time):
    print(0)
elif (s < Apple_time):
    APPLE_meichiwan = Apple_time - s #已经花费的时间
    APPLE_shengxia =  APPLE_meichiwan / t
    print(int(APPLE_shengxia))