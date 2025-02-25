"""
格式化输出

https://docs.python.org/zh-cn/3.13/library/string.html#formatspec
"""



# 测试
print("输出 二进制 类型: ")
print(format(10, "b"))

print("输出 unicode 类型: ")
print(format(98, "c"))

print("输出 十进制 类型: ")
print(format(98, "d"))

print("输出 八进制 类型: ")
print(format(98, "o"))

print("输出 浮点数 科学计数法表示: ")
print(format(98, "e"))

print("输出 浮点数 科学计数法表示,默认6位精度: ")
print(format(98, "f"))

print("输出 百分比")
print(format(0.001, "%"))


# 测试结果
"""
输出 二进制 类型: 
1010
输出 unicode 类型:
b
输出 十进制 类型:
98
输出 八进制 类型:
142
输出 浮点数 科学计数法表示:
9.800000e+01
输出 浮点数 科学计数法表示,默认6位精度:
98.000000
输出 百分比
0.100000%
"""