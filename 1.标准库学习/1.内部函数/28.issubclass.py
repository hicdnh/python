"""
判断类是否是某个类的子类
"""

class T:
    def __init__(self):
        pass

class SubClass(T):
    def __init__(self):
        super().__init__()

# 测试
print("判断SubClass()是否是T的子类的实例: %s" % issubclass(SubClass, T))


# 测试结果
"""
判断SubClass()是否是T的子类的实例: True
"""