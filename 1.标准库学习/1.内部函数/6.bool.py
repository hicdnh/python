"""
判断对象的所有元素都为真值
入参：
可迭代对象
"""

lst_true = [
    1, 2, 3
]

lst_false = [
    False
]

lst_empty = []

bool_true = True
bool_false = False

# 测试
print(bool(lst_true))
print(bool(lst_false))

print(bool(lst_empty))

print(bool(bool_true))
print(bool(bool_false))

# 测试结果
"""
True
True
False
True
False
"""