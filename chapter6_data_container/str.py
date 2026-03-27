message = '我是大官人'
# print(message.index('你'))
print(message.index('我'))

# index 方法：获取指定字符，在字符串中第一次出现的下标，没找到旧报错
msg = 'welcome to atguigu'
result = msg.index('t')
print(result)  # 8

msg = 'welcome to atguigu'
result = msg.count('g')
print(result)  # 2


# strip 方法：从某个字符串中删除：指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在字符串中的字符就停下
msg = '666尚6硅6谷666'
result = msg.strip('6')
print(msg)    # 666尚6硅6谷666
print(result) # 尚6硅6谷

msg = '1234尚12硅34谷4321'
result = msg.strip('1324')
print(msg)     # 1234尚12硅34谷4321
print(result)  # 尚12硅34谷

msg = '34215尚12硅34谷4132'
result = msg.strip('5432')
print(msg)   # 34215尚12硅34谷4132
print(result)# 15尚12硅34谷41

msg = '  尚硅谷  '
result = msg.strip()
print(msg)   #   尚硅谷
print(result)# 尚硅谷

# len 函数：统计字符串中字符的个数（字符串长度）
msg = 'welcome to atguigu'
result = len(msg)
print(result) # 18

msg = 'welcome to atguigu'
# while循环遍历
index = 0
while index < len(msg):
    print(msg[index])
    index += 1
msg = 'welcome to atguigu'

# for循环遍历
for item in msg:
    print(item)

# for循环遍历
for index,item in enumerate(msg):
    print(f'{index},{item}')