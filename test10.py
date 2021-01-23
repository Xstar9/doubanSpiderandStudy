dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,"1":5}
print(dict)

# 12.字典2 ：给第11题的字典后面添加一个键值对,更改第一个键值对的值为‘zero’
dict['g'] = 7
dict['a'] = "zero"
print(dict)

# 13.字典3 ：使用for循环取出经过第12问处理后的字典的所有键、值
for key in dict:
    print(key,dict[key])
    print(key)
