"""
判断对象类型
"""

class T:
    def __init__(self):
        pass

class SubClass(T):
    def __init__(self):
        super().__init__()

# 测试
print("判断T()是否是T的实例: %s" % isinstance(T(), T))
print("判断SubClass是否是T的实例: %s" % isinstance(SubClass(), T))


# 测试结果
"""
判断T()是否是T的实例: True
判断SubClass是否是T的实例: True
"""