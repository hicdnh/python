"""
返回基于一个数字或字符串构建的浮点数

inf表示无穷大
"""



# 测试
print("构建1个 正的 浮点数: ")
print(float("+1.24"))

print("科学计数法表示的字符串 构建1个 浮点数: ")
print(float("+3e-3"))
print(float("+3e+3"))
print(float("+3e-003"))

print(float('Inf'))
float('-Infinity')
# 测试结果
"""
0.003
3000.0
0.003
inf
"""