"""
返回一个迭代器对象
使用的地方不多

构建块读取器,例如，从二进制数据库文件中读取固定宽度的块，直至到达文件的末尾:
"""

from functools import partial

def process_block():
    pass


with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)