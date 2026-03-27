nums = (20,330,342,234)
print(type(nums))
print(nums)


print(nums[0])
print(nums[-1])

# nums.append(20)
# print(nums)

print(len(nums))
print(max(nums))
print(min(nums))

# print(nums.sort())
print(sorted(nums))

print(sum(nums))

nums = ()
print(type(nums))

nums = tuple()
print(type(nums))

# 定义一个元素的元组，后面必须根逗号，否则默认是数据类型
nums = (10,)
# nums[0] = 20  不允许修改 # 'tuple' object does not support item assignment
print(type(nums))
nums = (10)
print(type(nums)) # <class 'int'>


# 实际开发中的元组，不一定是我们自己定义的，比如函数的可变参数*args就是一个元组
def demo(*args):
    return sum(args)
result = demo(100, 200, 300)
print(result)  # 600

# 由于元组不可修改，所以它的常用方法只有两个：
# index 方法：获取指定元素在元组中第一次出现的下标。
t1 = (28, 67, 21, 67, 11)
result = t1.index(67)
print(result)  # 1

# 由于元组不可修改，所以它的常用方法只有两个：
# count 方法：统计指定元素在元组中出现的次数。
t1 = (28, 67, 21, 67, 11)
result = t1.count(67)
print(result)  # 2

index = 0
while index < len(t1):
    print(t1[index])
    index +=1
for item in t1:
    print(item)

for index,item in enumerate(t1,start=5):
    print(f'{index},{item}')


# 定义函数时，使用*args（变量不一定非要用args，比如写：*data也行），将收到的多个参数，打包成一个元组
def test(*args):
    print(f'我是test函数，我收到的参数是：{args}，参数类型是：{type(args)}')

list1 = [100, 200, 300, 400]
tuple1 = ('你好', '北京', '尚硅谷')

# 函数调用时，正常传递：列表 或 元组
# test(list1)
# test(tuple1)

# 函数调用时，使用*对：列表 或 元组进行解包后，再传递参数
test(*list1)  # 此种写法相当于：test(100, 200, 300, 400)
test(*tuple1)  # 此种写法相当于：test('你好', '北京', '尚硅谷')