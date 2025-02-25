"""
判断对象类型，但是不考虑子类的情况，所以不建议使用，推荐isinstance
"""

class T:
    def __init__(self):
        pass

class SubClass(T):
    def __init__(self):
        super().__init__()

s = SubClass()

print(type(s))
"""
<class '__main__.SubClass'>
"""