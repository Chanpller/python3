a = 10

def print_a(a):
    a += 1
    print(a)

print_a(1)
print(a)

a = 10

def print_a(c):
    global a
    a +=1
    print(a)

print_a(1)
print(a)


# 全局作用域 与 局部作用域，以及global的使用
a = 100
b = 200

def test():
    c = '尚硅谷'
    d = '你好啊'
    global a
    a = 300
    print('函数中的打印（a）', a)
    print('函数中的打印（b）', b)
    print('函数中的打印（c）', c)
    print('函数中的打印（d）', d)
test()
print('*')
print('全局的打印（a）', a)
print('全局的打印（b）', b)


# 函数嵌套调用测试1
def greet(name, msg):
    print(f'我叫{name}，我想说的话在下面：')
    speak(msg)
    print('嗯，我想说的结束了')

def speak(msg):
    print('----------')
    print(msg)
    print('----------')

greet('张三', '你好啊')

# 函数嵌套调用测试2
def test1():
    print('进入 test1 函数')
    test2()
    print('退出 test1 函数')

def test2():
    print('进入 test2 函数')
    test3()
    print('退出 test2 函数')

def test3():
    print('进入 test3 函数')
    print('*正在执行 test3 函数')
    print('退出 test3 函数')

test1()