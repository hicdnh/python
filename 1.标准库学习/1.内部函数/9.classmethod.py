"""
类方法装饰器
但要和Java和C++的静态方法区分开
python的类方法,不是静态方法；
"""

class C:
    @classmethod
    def class_method(cls):
        return 'abc'

# 测试
print(C.class_method())
print(C().class_method())

# 测试结果
"""
abc
abc
"""