"""
返回 number 舍入到小数点后 ndigits 位精度的值

在处理浮点数的时候，往往结果和预期不一样，需要认真阅读文档后再使用
https://docs.python.org/zh-cn/3.13/tutorial/floatingpoint.html#tut-fp-issues

"""



# 测试
print(round(10.222))
print(round(10.222, 1))

# 测试结果
"""
10
10.2
"""
