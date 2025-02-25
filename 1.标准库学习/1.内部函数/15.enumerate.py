"""
返回一个枚举对象
"""

lst = ['a', 'b', 'c', 'd']

# 测试
print(list(enumerate(lst)))
print(list(enumerate(lst, start=2)))


# 测试结果
"""
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
[(2, 'a'), (3, 'b'), (4, 'c'), (5, 'd')]
"""