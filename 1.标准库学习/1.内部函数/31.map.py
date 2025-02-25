"""
将 function 应用于 iterable 的每一项;并且返回结果
"""

num_lst = [1, 2, 3]

def add(a):
    return a + 1

# 测试
for i in map(add, num_lst):
    print(i)

# 测试结果
"""
2
3
4
"""

