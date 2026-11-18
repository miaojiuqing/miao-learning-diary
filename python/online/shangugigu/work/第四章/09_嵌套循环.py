# # for循环实现
# day = 1
# for day in range(1,31):
#     print(f'********📅第{day}天********')
#     for zu in  range(1,6):
#         print(f'💪这是第{zu}组仰卧起坐')
#     print('今日目标已达成')
# print(f'恭喜你,{day}天目标已全部完成')

# while循环实现
day = 1
while day <=30:
    print(f'********📅第{day}天********')
    zu = 1
    while zu <=5:
        print(f'💪这是第{zu}组仰卧起坐')
        zu += 1
    print('今日目标已达成')
    day += 1
print(f'恭喜你,{day - 1}天目标已全部完成')