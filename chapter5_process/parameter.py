# 定义函数（使用/和*限制传参方式）
def greet(name, /, gender, *, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

# 正确示例
greet('张三', '男', age=18, height=172)
greet('张三', gender='男', age=18, height=172)

# 错误示例
# greet(name='张三', gender='男', age=18, height=172)
# greet('张三', '男', 18, height=172)


# 定义函数（设置参数默认值）
def greet(name, gender, age, height, msg='你好'):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我想说：{msg}')


# 调用函数
greet('张三', '男', 18, 172)
greet('张三', '男', 18, 172, 'hello')
greet('张三', '男', 18, 172, msg='hello')


# 定义函数（使用*args去接收：可变位置参数，args只是大家习惯这么写，当然也可以换成其他变量）
def test1(*args):
    # 此处args的值，是一种新的数据类型，叫：元组，我们下一章就去讲元组
    print(args)

# 调用函数
test1('张三', '男', 18, 172)
# 定义函数（使用kwargs去接收：可变关键字参数，kwargs只是大家习惯这么写，当然也可以换成其他变量）
def test2(**kwargs):
    # 此处kwargs的值，是一种新的数据类型，叫：字典，我们下一章就去讲字典
    print(kwargs)

# 调用函数  错误参数
test2(name='张三', gender='男', age=18, height=172)


# 定义函数（同时使用：可变位置参数、可变关键字参数）
def test3(a, b, *args, c='尚硅谷', **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
# 调用函数
test3('张三', '男', '抽烟', '喝酒', age=18, height=172)

print('=======test4=========')
# 定义函数（同时使用：可变位置参数、可变关键字参数）
def test4(a, *args, b,c='尚硅谷',**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test4('张三', '男', '抽烟', b='喝酒', c=18, height=172)
