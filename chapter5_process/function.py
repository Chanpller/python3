def test():
    print("hello word")
# 需要先定义在使用
test()

def order(num,dish):
    print(f'您点的是：{num}份 {dish}')
    print(f'{dish}可是很好吃的！')
    print(f'你只点了{num}份，够吃吗？\n')
# 需要先定义在使用
order(1,'辣椒炒肉')
# order(num=2,'辣椒炒肉2') 错误写法
# order(1) 错误写法
# order('辣椒炒肉2') 错误写法
# order(dish='辣椒炒肉2') 错误写法
#  order(num='辣椒炒肉2')错误写法
order(num=2,dish='辣椒炒肉2')
order(3,dish='辣椒炒肉3')
order(dish='辣椒炒肉4',num=4)

