"""
虽然被称为函数，但 range 实际上是一个不可变的序列类型
"""



# 测试
for i in range(3):
    print(i)

print("=======")

for j in range(10, 20, 5):
    print(j)

# 测试结果
"""
0
1
2
=======
10
15
"""
