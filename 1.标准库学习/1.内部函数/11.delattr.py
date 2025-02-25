"""
删除对象某个属性
入参：对象，属性名字
"""


class T:
    A = 100
    B = 200


# 测试
t = T()
print(t.A)
delattr(t, 'A')
print(t.A)

# 测试结果
"""
# 删除前属性A可以使用
100

# 删除后,报错没有属性A
Traceback (most recent call last):
  File "d:\repo\github\python\1.标准库学习\1.内部函数\11.delattr.py", line 15, in <module>
    delattr(t, 'A')
    ~~~~~~~^^^^^^^^
AttributeError: 'T' object has no attribute 'A'
"""