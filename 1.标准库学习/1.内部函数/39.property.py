"""
托管属性
"""


# 使用property定义托管属性
class PropertyTest:
    def __init__(self):
        self._x = None
    
    def pget(self):
        return self._x
    
    def pset(self, v):
        self._x = v
    
    def pdel(self):
        del self._x
    x = property(pget, pset, pdel, "test")

# 测试
p1 = PropertyTest()
p1.x = 1
print(p1.x)

# 测试结果
"""
1
"""


# 使用装饰器定义托管属性

class PropertyTestDec:
    def __init__(self):
        self._x = None
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, v):
        self._x = v
    
    @x.deleter
    def x(self):
        del self._x

# 测试
p2 = PropertyTestDec()
p2.x = 1
print(p2.x)

# 测试结果
"""
1
"""