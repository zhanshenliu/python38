
a = "xiaozhang"
b = '147258'
name = input('请输入登录名')
pwd = input('请输入登录密码')
if a == name:
    if b == pwd:
        print('欢迎回来')
    else:
        print('登录名或者密码错误')

