"""
判断对象是否能被调用
入参：object
"""

lst = [
    1, 2, 3
]

class TestFalse:
    def __init__(self):
        pass

class TestTrue:
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwds):
        pass


# 测试
print(callable(lst))
print(callable(TestFalse()))
print(callable(TestTrue()))

# 测试结果
"""
False
False
True
"""