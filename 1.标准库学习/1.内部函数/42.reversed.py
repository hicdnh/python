"""
返回一个反向的迭代器
"""

lst = [1, 2, 3]

# 测试
iter_test = reversed(lst)

for i in iter_test:
    print(i)


# 测试结果
"""
3
2
1
"""
