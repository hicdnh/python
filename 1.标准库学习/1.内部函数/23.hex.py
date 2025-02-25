"""
转为16进制数
"""


# 测试
print(hex(100))
print(hex('abc'))

# 测试结果

"""
0x64

Traceback (most recent call last):
  File "d:\repo\github\python\1.标准库学习\1.内部函数\23.hex.py", line 8, in <module>
    print(hex('abc'))
          ~~~^^^^^^^
TypeError: 'str' object cannot be interpreted as an integer
"""