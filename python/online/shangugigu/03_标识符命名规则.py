# ===================== Python标识符命名规则笔记 =====================
# 标识符：变量、函数、类等的名字
# 命名三大规范：大驼峰、小驼峰、蛇形命名（Python变量推荐蛇形 snake_case）

# ---------------------- 基础合法命名示例 ----------------------
name2 = '张三'
age_2 = 18
_weight_ = 60.2

name = '熊大'
Name = '熊二'

# 三种命名风格
userName = '刘海柱'      # 小驼峰(lowerCamelCase)：第一个单词首字母小写，后面单词首字母大写
UserName = '刘海柱'      # 大驼峰(UpperCamelCase)：所有单词首字母大写（Python一般用于类名）
user_name = '刘海柱'     # 蛇形(snake_case)：多个单词之间用下划线分隔，Python变量推荐！


# ---------------------- 命名对照表 ----------------------
"""
中文含义	        大驼峰	            小驼峰	            蛇形
学生成绩	        StudentScore	    studentScore	    student_score
是否登录	        IsLoggedIn	        isLoggedIn	        is_logged_in
用户邮箱地址	    UserEmailAddress	userEmailAddress	user_email_address
文件上传路径	    FileUploadPath	    fileUploadPath	    file_upload_path
最大重试次数	    MaxRetryCount	    maxRetryCount	    max_retry_count
"""

# ---------------------- Python命名习惯补充 ----------------------
# ✅ 变量、函数：优先使用蛇形命名 snake_case
# ✅ 类名：优先使用大驼峰 UpperCamelCase
# ✅ 常量：全部大写，下划线分隔 MAX_RETRY_COUNT
# ❌ 不能用中文、空格、特殊符号；不能数字开头；不能用Python关键字做变量名
