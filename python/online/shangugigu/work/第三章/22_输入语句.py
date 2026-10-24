#使用input()获取用户的输入name 
#input()获取到的内容全都是字符串类型
name = input("请输入你的名字：")
age = input("请输入你的年龄：")

#将age转为整型
age = int(age)

#打印信息
print(f"{name},你的年龄是{age}岁")
print(f"{name},我夜观天象卜得一卦，你明年的年龄是{age + 1}")