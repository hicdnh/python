"""
 filter(function, iterable) 相当于一个生成器表达式
 
 当 function 不是 None 的时候为 (item for item in iterable if function(item))；function 是 None 的时候为 (item for item in iterable if item) 
"""