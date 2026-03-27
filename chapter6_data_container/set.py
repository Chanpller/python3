
set1 = {100,56,54,100,65,78,54}

print(type(set1))
print(set1)

set2 = set()
print(type(set2))
print(set2) # set()

# 不能直接写{}来定义空集合，因为直接写{}定义的是：空字典
s2 = {}
print(type(s2), s2)  # <class 'dict'> {}

# 定义有内容的【不可变集合】
s1 = frozenset({10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100})
s2 = frozenset({'你好', 'hello', '你好', 'atguigu', '北京'})
s3 = frozenset({10, '你好', True, 1, 12.4})
print(type(s1), s1)
print(type(s2), s2)
print(type(s3), s3)

# frozenset 接收的参数，可以是任意可迭代对象，但最终返回的一定是【不可变集合】
s1 = frozenset([10, 20, 30, 40, 50])
s2 = frozenset((10, 20, 30, 40, 50))
s3 = frozenset('hello')
print(type(s1), s1)
print(type(s2), s2)
print(type(s3), s3)

# 定义空集合（不可变集合）
s3 = frozenset()
print(type(s3), s3)


# 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】
# 通俗理解：只有“不可变”的东西，才能安全的放进集合里
s1 = {10, 20, 30, 40, 50}
s2 = frozenset({100, 200, 300, 400, 500})
l1 = [666, 777, 888]
t1 = ('hello', 'atguigu', '北京')

# s3 = {11, 22, 33, s1}  # 报错
s3 = {11, 22, 33, s2}  # 没问题
# s3 = {11, 22, 33, l1}  # 报错
s3 = {11, 22, 33, t1}  # 没问题
print(s3)


s1 = {10, 20, 30, 40, 50}
s1.update([20, 60, 80])
s1.add(60)
print(s1)


# remove方法：从集合中移除元素（移除不存在的元素，会报错）
s1 = {10, 20, 30, 40, 50}
s1.remove(20)
print(s1)

# discard方法：从集合中移除元素（移除不存在的元素，不会报错）
s1 = {10, 20, 30, 40, 50}
s1.discard(80)
print(s1)

# pop方法：从集合中移除一个任意元素，返回值是移除的那个元素
s1 = {10, 20, 30, 40, 50}
s2 = {'你好', '北京', '尚硅谷', 'hello'}
result = s1.pop()
print(s1)
print(result)

# clear方法：清空集合
s1 = {10, 20, 30, 40, 50}
s1.clear()
print(s1)

# 改
# 使用 add + remove 的组合，来实现修改的效果
s1 = {10, 20, 30, 40, 50}
s1.remove(20)
s1.add(66)
print(s1)


# 查：集合不能通过下标去读取元素，但能通过 【成员运算符】去查看集合中是否包含指定元素
# 由于成员运算符适用于所有数据容器，所以我们会等所有数据容器都讲完以后，再说成员运算符
s1 = {10, 20, 30, 40, 50}
# s1[0] # 此行报错，因为集合不能通过下标访问元素

# 先提前感受一下成员运算符
result = 20 not in s1
print(result)
