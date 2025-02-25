"""
将 source 编译成代码或 AST 对象，用eval或者exec方法执行
入参: 文件或者字符串

需要特别注意:
在将足够大或者足够复杂的字符串编译成 AST 对象时，Python 解释器有可能因为 Python AST 编译器的栈深度限制而崩溃。
"""


text_code = """
print(1234567)
"""

# 测试
code = compile(text_code, filename='', mode='eval')
print(exec(code))


# 测试结果
"""
1234567
None
"""