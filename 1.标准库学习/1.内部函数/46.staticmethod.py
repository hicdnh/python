"""
静态方法,和Java、C++的类似
"""

class StaticM:
    def __init__(self):
        pass

    @staticmethod
    def get(name=None):
        return name
print(StaticM.get("b"))

"""
b
"""

# 使用托管的方式
def get(name=None):
    return name

class StaticMethod:
    def __init__(self):
        pass
    get_property = staticmethod(get)


print(StaticMethod.get_property(name='abc'))

"""
abc
"""