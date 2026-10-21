day = input("今天星期几？\n支持英文/中文/阿拉伯数字\n请输入：").strip()

if day in ("Monday", "1", "一"):
    print("新的一周，新的开始，加油工作！")
elif day in ("Tuesday", "2", "二"):
    print("第二天，保持节奏，稳步推进！")
elif day in ("Wednesday", "3", "三"):
    print("周中了，坚持一下！")
elif day in ("Thursday", "4", "四"):
    print("再撑一天，周末就在眼前！")
elif day in ("Friday", "5", "五"):
    print("周末将至，准备放松！")
elif day in ("Saturday", "6", "六"):
    print("休息日，好好犒劳自己！")
elif day in ("Sunday", "7", "日", "天"):
    print("周末结束，准备迎接新一周。")
else:
    print("继续执行您的日常任务。")

print("感谢您使用我们的周日活动建议程序！")