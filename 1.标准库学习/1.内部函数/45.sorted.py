"""
排序
https://docs.python.org/zh-cn/3.13/howto/sorting.html#sortinghowto

"""

# 列表排序
lst = [13, 2, 3]
print(sorted(lst))
# 排序结果 [2, 3, 13]

# 对象排序

class Student:
    def __init__(self):
        self._name = None
        self._age = None
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v
    
    @name.deleter
    def name(self):
        del self._name
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, v):
        self._age = v
    
    @age.deleter
    def age(self):
        del self._age

s1 = Student()
s2 = Student()
s3 = Student()

s1.name = "李雷"
s1.age = 10

s2.name = "韩梅梅"
s2.age = 12

s3.name = "Lucy"
s3.age = 9

student_lst = [
    s1, s2, s3
]

print("===========")
sorted_student_lst = sorted(student_lst, key=lambda s: s.age)
for stu in sorted_student_lst:
    print(stu.name)

"""
排序结果
Lucy
李雷
韩梅梅
"""