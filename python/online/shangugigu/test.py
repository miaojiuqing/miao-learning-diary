name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
professional = input("请输入您的专业：")
grades = input("请输入您的成绩：")

# 进行类型转换（注意：年龄用 int，成绩用 float）
age_z = int(age) 
grades_z = float(grades)

# 在打印时，记得使用转换后的变量名 (age_z, grades_z)，这样输出才准确
print(f"专业为{professional}的{age_z}岁学生{name}的成绩是：{grades_z}分")