"""
判断对象是否有某个属性
"""

class T:
    a = 1


# 测试
print(hasattr(T(), 'a'))

# 测试结果
"""
True
"""