s1 = {10, 20, 30, 40, 50, 60}

# 集合不能使用while循环遍历（以下是错误示例）
# index = 0
# while index < len(s1):
#     print(s1[index])
#     index += 1

# 集合可以使用for循环遍历
for item in s1:
    print(item)

# s1 = {10, 20, 30, 40, 50, 60}
# s2 = {40, 50, 60, 70, 80, 90}
#
# # 并集
# result = s1 | s2
# print(result) # {70, 40, 10, 80, 50, 20, 90, 60, 30}
#
# # 交集
# result = s1 & s2
# print(result) # {40, 50, 60}
#
# # 差集
# result = s1 - s2
# print(result) # {10, 20, 30}
#
# # 对称差集
# result = s1 ^ s2
# print(result) # {70, 10, 80, 20, 90, 30}

# # 集合A.isdisjoint(集合B)：
# # 作用：
# # 如果没有交集，返回True；只要有一个公共元素，就返回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {80, 90}
# result = s1.isdisjoint(s3)
# print(result)

# # 集合A.issuperset(集合B)：
# # 作用：判断集合A是否是集合B的超集
# # 如果集合A中，包含了集合B中的所有元素，那就返回True，否则返回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {30, 40, 50}
# result = s1.issuperset(s3)
# print(result)
#
# # 集合A.issubset(集合B)：
# # 作用：判断集合A是否为集合B的子集
# # 如果 集合A的所有元素都在集合B中，那就返回True，否则返回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {30, 40, 50}
# result = s3.issubset(s1)
# print(result)

# # 集合A.union(集合B)：
# # 作用：合并两个集合，集合A 和 集合B 都不变，返回的是一个新的集合
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# result = s2.union(s1)
# print(s1)
# print(s2)
# print(result)

# # 集合A.difference_update(集合B)：
# # 作用：从集合A中，删除集合B中存在的元素（集合A会被修改，集合B不会）
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s1.difference_update(s2)
# print(s1)
# print(s2)

# # 集合A.difference(集合B)：
# # 作用：找出集合A中，不同于集合B的元素（集合A 与 集合B 都不变，返回的是一个新的集合）
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# result = s1.difference(s2)
# print(s1)
# print(s2)
# print(result)

#
# set1 = {100,56,54,100,65,78,54}
#
# print(type(set1))
# print(set1)
#
# set2 = set()
# print(type(set2))
# print(set2) # set()
#
# # 不能直接写{}来定义空集合，因为直接写{}定义的是：空字典
# s2 = {}
# print(type(s2), s2)  # <class 'dict'> {}
#
# # 定义有内容的【不可变集合】
# s1 = frozenset({10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100})
# s2 = frozenset({'你好', 'hello', '你好', 'atguigu', '北京'})
# s3 = frozenset({10, '你好', True, 1, 12.4})
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)
#
# # frozenset 接收的参数，可以是任意可迭代对象，但最终返回的一定是【不可变集合】
# s1 = frozenset([10, 20, 30, 40, 50])
# s2 = frozenset((10, 20, 30, 40, 50))
# s3 = frozenset('hello')
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)
#
# # 定义空集合（不可变集合）
# s3 = frozenset()
# print(type(s3), s3)
#
#
# # 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】
# # 通俗理解：只有“不可变”的东西，才能安全的放进集合里
# s1 = {10, 20, 30, 40, 50}
# s2 = frozenset({100, 200, 300, 400, 500})
# l1 = [666, 777, 888]
# t1 = ('hello', 'atguigu', '北京')
#
# # s3 = {11, 22, 33, s1}  # 报错
# s3 = {11, 22, 33, s2}  # 没问题
# # s3 = {11, 22, 33, l1}  # 报错
# s3 = {11, 22, 33, t1}  # 没问题
# print(s3)
#
#
# s1 = {10, 20, 30, 40, 50}
# s1.update([20, 60, 80])
# s1.add(60)
# print(s1)
#
#
# # remove方法：从集合中移除元素（移除不存在的元素，会报错）
# s1 = {10, 20, 30, 40, 50}
# s1.remove(20)
# print(s1)
#
# # discard方法：从集合中移除元素（移除不存在的元素，不会报错）
# s1 = {10, 20, 30, 40, 50}
# s1.discard(80)
# print(s1)
#
# # pop方法：从集合中移除一个任意元素，返回值是移除的那个元素
# s1 = {10, 20, 30, 40, 50}
# s2 = {'你好', '北京', '尚硅谷', 'hello'}
# result = s1.pop()
# print(s1)
# print(result)
#
# # clear方法：清空集合
# s1 = {10, 20, 30, 40, 50}
# s1.clear()
# print(s1)
#
# # 改
# # 使用 add + remove 的组合，来实现修改的效果
# s1 = {10, 20, 30, 40, 50}
# s1.remove(20)
# s1.add(66)
# print(s1)
#
#
# # 查：集合不能通过下标去读取元素，但能通过 【成员运算符】去查看集合中是否包含指定元素
# # 由于成员运算符适用于所有数据容器，所以我们会等所有数据容器都讲完以后，再说成员运算符
# s1 = {10, 20, 30, 40, 50}
# # s1[0] # 此行报错，因为集合不能通过下标访问元素
#
# # 先提前感受一下成员运算符
# result = 20 not in s1
# print(result)
