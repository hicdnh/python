"""
返回包含一个对象的可打印表示形式的字符串
"""

class Dog:
    def __init__(self):
        self._age = 10
        self._weight = 100

    def __repr__(self):
        return "对象地址:%s-age:%d-weight:%d" % (id(self), self._age, self._weight)


# 测试
print(Dog())

# 测试结果
"""
对象地址:2159466671680-age:10-weight:100
"""
