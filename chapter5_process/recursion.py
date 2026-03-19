def welcome(n):
    if n > 1:
        welcome(n - 1)
    print(f'你好啊！第{n}次')

def welcomereserve(n):
    print(f'你好啊！第{n}次')
    if (n > 1):
        welcome(n - 1)
welcome(5)
print('=========================')
welcomereserve(5)

def factorial(n):
    """
    这是一个阶乘方法
    :param n: n表示阶乘数
    :return: 返回阶乘结果
    """
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n = 4
print(f'{n}的阶乘结果为：{factorial(n)}')


