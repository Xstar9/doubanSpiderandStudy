# 1.分别定义一个整型、浮点型、字符型、布尔型的数据 并输出
i = int(666)
print(i)
f = float(6.666)
print(f)
s = str('six')
print(s)
b = bool(0)
b1 =bool(1)
print(b,b1)

# 2.使用if...elif...else...语句格式 ：通过表达式评估一个语句真或假
j = 66
k = 6
if j%k == 0:
    print(j/k)
elif j*k >= 100:
    print('true')
else:
    print('false')

# 3.使用while循环 ：使用while循环输出[10,20]，11个数
i = 10
while(i<=20):
    print(i)
    i += 1

# 4.深入理解while循环 ：使用while循环输出11,9,7,5,3,1
j = 11
while(j > 0):
    print(j)
    j -= 2

# 5.使用for循环 ：使用for循环实现第3题
for i in range(10,20+1):
    print(i)

# 6.深入理解for循环 ：使用for循环实现第4题
for k in range(11,0,-2):
    print(k)

# 7.列表1 ：定义一个列表,要求整型、浮点型、字符型数据各两个，使用ap
list = []
list.append(6)
list.append(66)
list.append(6.66)
list.append(66.66)
list.append('six')
list.append('sixty-six')
print(list)

# 8.列表2：定义一个新列表与第7题的列表合并,要求第8题列表在前
list1 = [5,55,5.5,55.55,'five','fifty-five']
list1.extend(list)
print(list1)

# 9.列表3 ：删除第8问中合并链列表的后4个数据
del list1[len(list1)-4:len(list1)]
print(list1)

# 10.元组 ：定义一个不小于5个值的元组，取出其中的第1、3、5位
tup = (6,6.6,'c++','java','python')
print("tup第1、3、5位:",tup[0:5:2])

# 11.字典1 ：定义一个字典，要求其中键值对不小于6个
dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
print(dict)

# 12.字典2 ：给第11题的字典后面添加一个键值对,更改第一个键值对的值为‘zero’
dict['g'] = 7
dict['a'] = "zero"
print(dict)

# 13.字典3 ：使用for循环取出经过第12问处理后的字典的所有键、值
for key in dict:
    print(key,dict[key])
    

# 14.list使用深层拷贝与浅层拷贝，对比他们有什么不同
import copy

# 直接赋值
list2 = list
print(list2)
list.append('new')
print(list2)    # list改变，list2也改变
list2.append('new1')
print(list)     # list2改变，list也改变
# 浅层
list2.append(['a','b'])
list3 = copy.copy(list2)
print(list3); print(list2)   # 浅层复制
list2.append('new2')
print(list2); print(list3)    # 浅层下，list2添加元素，list3不改变
list3[-1].append('c')
print(list2); print(list3)     # 浅层下，list3中的元素子列表中添加'c',list2中的子列表也改变
# 浅层拷贝未拷贝到子对象

# 深层
list4 = copy.deepcopy(list3)
list3.append('new3')
print(list3); print(list4)  # 深层拷贝下，list3添加元素，list4拷贝不变
list3[-2].append('d')
print(list3); print(list4)  # 深层拷贝下，list3子列表添加元素，list4不变
# 深层拷贝的列表不会随原列表变化而改变

# 15.文件 ：新建一个名字叫name的txt文件
# 在其中写入你的班级、姓名、学号、要求每个数据占用一行
filew = open('name.txt','w')
filew.write('Class:软件1805'+'\n')
filew.write('Name:zhengxin'+'\n')
filew.write('ID:5120181014'+'\n')
filew.close()

filer = open('name.txt','r')
line = filer.read()
print(line)
filer.close()

# 16.练习题
'''
题目描述：打印杨辉三角前 5 行
结果应如下：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
num = int(5)
list5 = []
for n in range(num):
    r = [1]      # 记录每行
    list5.append(r)

    if(n == 0):    # 第一行
        print(r)
        continue
    for m in range(1,n):
        r.append(list5[n-1][m-1]+list5[n-1][m])
    r.append(1)
    # print(r)  打印列表
# 打印5行杨辉三角
for i in range(num):
    for j in range(i+1):
        print(list5[i][j],end='\t')
    print()

# 17.练习题
'''
交换 var3 和 var4 的值
var3 = 5
var4 = 6
'''
def fun(x,y):
    x,y = y,x
    print(x,y)
var3 = 5
var4 = 6
fun(var3,var4)

# 18.练习题
'''
写一个函数来数每一个字母在下面这个 list 里面出现了几次，并把结果打印出来
my_list = ['a', 'b', 'c', 'a', 'b', 'a','2','f','2','f']
'''
def func(_list):
    count = {}
    list6 = copy.copy(_list)
    for i in list6:
            if i not in count:
                count[i]=1
            else:
                count[i] +=1
    print(count)

my_list = ['a', 'b', 'c', 'a', 'b', 'a','2','f','2','f']
func(my_list)

# 19.练习题
'''
求1—100所有偶数的和，使用本节课学到的循环语句(while, for)
注：写一个for一个while哦
'''
number = 0
sum = 0
while number <= 100:
    number += 1
    if number%2 == 0 :
        sum += number
    else:
        continue
print(sum)
'''------------while-------------------'''
sum1 = 0
for numb in range(0,100+1,2):
    sum1 += numb
print(sum1)
'''-------------for------------------------'''

# 20.时间戳 ：使用时间戳，输出当前秒数和正常时间
import time
t = time.time()
print(t)
t_local =time.localtime(t)      # 当前时间
print(t_local)
T = time.strftime("%Y/%m/%d %H:%M:%S",t_local)   # 时间格式化
print(T)
t_array = time.strptime(T,"%Y/%m/%d %H:%M:%S")
Tstamp = time.mktime(t_array)
print(int(Tstamp))
# 时间转时间戳：time.time() ->  time.strptime() -> time.mktime() 时间->时间数组->时间戳


