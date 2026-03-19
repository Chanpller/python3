print('=======int转换========')
print(int(19.2))
print(int(True))
print(int(10))
print(int('11'))
print(int('12 '))
print(int(' 13 '))
# print(int(' 1 4 '))
# print(int(' 14个 '))
# print(int(' 14.6 '))
print('=======float转换========')
print(float(19.2))
print(float(True))
print(float(10))
print(float('11.3'))
print(float('12.4 '))
print(float(' 13.4 '))
# print(float(' 1 4 '))
# print(float(' 14个 '))
print(float(' 14.6 '))

print('=======str转换========')
print(str(19.2))
print(str(True))
print(str(10))
print(str('11.3'))
print(str('12.4 '))
print(str(' 13.4 '))
print(str(' 1 4 '))
print(str(' 14个 '))
print(str(' 14.6 '))

print('=======运算符========')
# 加
print(9 + 7)
# 减
print(7 - 2)
# 乘
print(3 * 4)
# 除
print(9 / 3)
# 取整
print(9 // 6)
# 取余
print(9 % 6)
# 指数
print(2 ** 3)

print('=======字符串比较========')
# 字符串进行比较时，是依次比较每个字符的 Unicode 编码。
# Unicode 编码是一种全球通用的字符编码标准，它会给每个字符都分配一个“身份证号”。
# 以上这些比较运算符，同样适用于字符串
msg1 = 'abc'
msg2 = 'abc666'
print(msg1 < msg2)

msg1 = 'abc'
msg2 = 'abc'
print(msg1 != msg2)

print('=======逻辑运算符========')
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print(8 > 7 and 8 > 7) # True
print(8 > 7 and 2 > 3) # False
print(2 > 3 and 8 > 7) # False
print(2 > 3 and 2 > 3) # False

#and具备“逻辑短路”能力，以下代码中包含3/0这种错误代码，但最终没有报错。
print(False and 3 / 0) # false
# print(True and 3 / 0) # 运行报错

print(True or 3 / 0) # false

print(not 3 / 1)

print('=======进制========')
# 0b开头表示二进制
num1 = 0b11001
# 0o开头表示八进制
num2 = 0o1034
# 0x开头表示十六进制
num3 = 0x1cf
print(num1)
print(num2)
print(num3)

# 二进制函数
print(bin(num1))
# 八进制函数
print(oct(num2))
# 十六进制函数
print(hex(num3))


age = int(input('请输入你的年龄：'))