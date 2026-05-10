# 定义有内容的字典
d1 = {'张三': 72, '李四': 60, '王五': 85,'李四': 80,}
print(type(d1), d1)


# 字典中的key必须是不可变类型，但value可以是任意类型
# 通俗理解：只有不可变的东西，才能作为key
d1 = {250: 72, '李四': 60, '王五': 85}
d2 = {('抽烟', '喝酒'): 72, '李四': 60, '王五': 85}
print(d1)
print(d2)

# 错误示例：将列表作为key，是不行的
# d2 = {{'抽烟', '喝酒'}: 72, '李四': 60, '王五': 85}
# d3 = {['抽烟', '喝酒']: 72, '李四': 60, '王五': 85}

# 新增
d1 = {'张三': 72, '李四': 60, '王五': 85}
d1['赵六'] = 100
print(d1)

# 删除
d1 = {'张三': 72, '李四': 60, '王五': 85}

# 删除指定key所对应的那组键值对
del d1['张三']
print(d1)

# 删除指定key所对应的那组键值对，并返回这个key所对应的值
# result = d1.pop('张三')
# print(d1)
# print(result)

result = d1.pop('奥特曼', '删除失败！')
print(d1)
print(result)

# 清空字典
d1.clear()
print(d1)


d1 = {'张三': 72, '李四': 60, '王五': 85}

# 修改的写法，与新增的写法一样，若字典中有对应的key，就是修改；若没有，就是新增
d1['张三'] = 97
print(d1)

# 批量修改
d1.update({'李四': 40, '王五': 67})
print(d1)


# 查询
d1 = {'张三': 72, '李四': 60, '王五': 85}

# 直接取值，若键（key）不存在，会报错
result = d1['张三']

# 安全取值，若键（key）不存在，会返回默认值（若没有设置默认值，则会返回None）
result = d1.get('奥特曼', '抱歉，key不存在！')
print(result)

# ==================================
# keys方法：用于获取字典中所有的键
d1 = {'张三': 72, '李四': 60, '王五': 85}

# keys方法的返回值不是list，而是一种叫做dict_keys的类型
result = d1.keys()
print(result)
print(type(result))

print('=========================')
# dict_keys和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
for item in result:
    print(item)

print('=========================')
# print(result[0]) 报错 dict_keys和列表类似 它不能通过下标访问元素

# 借助内置的list函数，可以将dict_keys转换成list
l1 = list(result)
print(l1)
print(type(l1))


print('=========================')
# values方法：获取字典中所有的值
d1 = {'张三': 72, '李四': 60, '王五': 85}
# values方法的返回值类型是：dict_values，它的特点和dict_keys一样
result = d1.values()
print(result)
print(type(result))


print('=========================')
# items方法：获取字典中所有的键值对（每组键值对以元组的形式呈现）
d1 = {'张三': 72, '李四': 60, '王五': 85}

# items方法返回的类型是：dict_items，它的特点也和dict_keys一样
result = d1.items()
print(result)
print(type(result))

print('=========================')
# 字典不能使用while循环遍历，但可以使用for循环遍历
d1 = {'张三': 72, '李四': 60, '王五': 85}

for key in d1:
    print(f'{key}的成绩是{d1[key]}')

for key in d1.keys():
    print(f'{key}的成绩是{d1[key]}')