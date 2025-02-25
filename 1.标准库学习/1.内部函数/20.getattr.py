"""
object 中指定名称的属性的值
"""

class T:
    a = 1


# 测试
print(getattr(T(), 'a'))

# 测试结果
"""
1
"""