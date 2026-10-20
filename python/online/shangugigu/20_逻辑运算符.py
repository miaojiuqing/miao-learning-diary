# and用于判断其两侧的值，是否都为True
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print(8 > 7 and 8 > 7)
# print(8 > 7 and 2 > 3)
# print(2 > 3 and 8 > 7)
# print(2 > 3 and 2 > 3)

# and具备“逻辑短路”能力
# print(False and 3 / 0)
# print(3 > 9 and 3 / 0)

# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则：and会先看左边，如果左边是“假”，就直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
print(2 - 2 and True)
print('' and True)
print(True and 8 / 2)
print(3 + 3 and 3 * 4)
