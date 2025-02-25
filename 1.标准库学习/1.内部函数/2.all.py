"""
判断对象的所有元素都为真值
入参：
可迭代对象
"""

lst_true = [
    1, 2, 3
]

lst_false = [
    1, 2, 3, []
]


# 测试
print(all(lst_true))
print(all(lst_false))

# 测试结果
"""
True
False
"""
