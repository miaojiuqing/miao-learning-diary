# 定义函数（使用/和*限制传参方式）
def auto (game,/,helper,*,comepany):
    print(f"游戏叫做{game}")
    print(f"助手是{helper}")
    print(f"游戏由{comepany}开发\n")

# 正确示例
auto("魔王与龙的建国谭","辛西娅小助手",comepany="万代")
auto("崩坏三","识宝小助手",comepany="米哈游")
auto("卡厄思梦境","维罗妮卡小助手",comepany="CM")
# 错误示例
# ##限制只能传指名却定位置
# auto("魔王与龙的建国谭","辛西娅小助手","万代")
# ##限制只能传位置却指名
# auto(game = "崩坏三",helper = "识宝小助手",comepany="米哈游")
# auto("卡厄思梦境","维罗妮卡小助手",comepany="CM")
