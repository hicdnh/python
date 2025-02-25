"""
在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组。
"""

lst = [
    1, 2, 3
]

name_lst = [
    "Lucy", "Lilei", "HanMeiMei"
]

for i in zip(lst, name_lst):
    print(i)

print(zip(lst, name_lst))

"""
(1, 'Lucy')
(2, 'Lilei')
(3, 'HanMeiMei')
<zip object at 0x0000017E9A80EB40>
"""