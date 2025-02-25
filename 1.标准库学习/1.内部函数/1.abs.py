"""
取绝对值函数
入参：
实现了__abs__()方法的对象
1)整数
2)浮点数
3)其他对象，如果实现了__abs__()方法，也可以
"""

class Test:
    def __init__(self):
        pass

    def __abs__(self):
        return 100
test = Test()


# 测试
print(abs(100))
print(abs(-100))
print(abs(100.1111))
print(abs(-100.1111))
print(abs(0))


print("输出实现了__abs__方法对象的绝对值")
print(abs(test))

# 测试结果
"""
100
100
100.1111
100.1111
0
输出实现了__abs__方法对象的绝对值
100
"""