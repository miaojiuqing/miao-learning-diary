# 使用 \' 输出 '
# print('在Python中，可以使用\'包裹一个字符串')

# 使用 \" 输出 "
# print("在Python中，可以使用\"包裹一个字符串")

# 使用 \n 进行换行
# print('注册会员需要以下信息：\n姓名\n年龄\n手机号')

# 使用 \\ 输出 \
# print('D:\\nice')

# 使用 \b 删除前一个字符
# print('helloo\b')

# 使用 \r 使光标回到本行开头，覆盖输出
# print('67%\r68%')

# 使用 \t 表示水平制表符（让光标跳转到下一个制表位）
# print('1234123412341234')
# print('ab\tcd')
# print('abc\td')
# print('abcd\ta')
# print('我是\t中文')

print('12341234123412341234')
print('姓名\t\t性别\t年龄')
print('李织烟\t\t女\t18')
print('尼古喵喵\t女\t25')
print('东方仗助\t男\t32')

# //拓展内容：
'''
# 打字机模拟
import time

time.sleep(5)
print("我正在输入：", end='', flush=True)
time.sleep(0.5)
print("你", end='', flush=True)
time.sleep(0.5)
print("好", end='', flush=True)
time.sleep(0.5)
print("牙", end='', flush=True)
time.sleep(0.5)
print("\b", end='', flush=True)
time.sleep(0.5)
print("呀", flush=True)

# 进度条加载
import time

time.sleep(5)
for i in range(1, 101):
    print(f"\r正在加载{i * 1}%", end='', flush=True)
    time.sleep(0.1)
'''