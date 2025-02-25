"""
所有类的基类,不接受任何参数

object 实例 没有 __dict__ 属性，因此你无法将任意属性赋给 object 的实例。
"""


# 测试
o = object()
setattr(o, 'a', 1)

# 测试结果
"""
Traceback (most recent call last):
  File "d:\repo\github\python\1.标准库学习\1.内部函数\34.object.py", line 10, in <module>
    setattr(o, 'a', 1)
    ~~~~~~~^^^^^^^^^^^
AttributeError: 'object' object has no attribute 'a' and no __dict__ for setting new attributes
"""

