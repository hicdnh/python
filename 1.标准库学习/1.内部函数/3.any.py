"""
判断对象的任意元素为真值
入参：
可迭代对象
"""

lst_true = [
    1, 2, 3, []
]

lst_false = [
    []
]


# 测试
print(any(lst_true))
print(any(lst_false))

# 测试结果
"""
True
False
"""
