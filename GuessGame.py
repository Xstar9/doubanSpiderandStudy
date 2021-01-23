# 猜拳程序
import random

flag = 1
while flag:
    print("你出什么？(0.石头 1.剪刀 2.布):")
    y = int(input())
    x = random.randint(0, 2)
    if x == y:
        print("x=%d y=%d" % (x, y))
        print("平局~")
    elif (x == 0 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 0):
        print("x=%d y=%d" % (x, y))
        print("你输了")
    else:
        print("x=%d y=%d" % (x, y))
        print("你赢了")
    print("再来一把？(0.不了 1.来嘛)")
    flag = int(input())


# 正反九九乘法表
for i in range(9, 0, -1):
    for j in range(1, i+1):
        k = i * j
        if j < i:
            print("%d*%d=%d" % (i, j, k), end=" ")
        elif j == i:
            print("%d*%d=%d" % (i, j, k))
for a in range(1, 10, 1):
    for b in range(1, a+1):
        k = a * b
        if b < a:
            print("%d*%d=%d" % (a, b, k), end=" ")
        elif j == i:
            print("%d*%d=%d" % (a, b, k))


#   \/  斜杠转义     \' 单引号转义   \" 双引号转义


# 列表List[]   相当于C数组，可修改

products = [["iphone", 6888], ["MacPro", 14800], ["XIaoMi6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
print("------商品列表------")
for i in range(len(products)):
    print("%d\t%s\t%d\t" % (i, products[i][0], products[i][1]))
flag = 1
Sum = 0
ShoppingChart = []
while flag != 'q':
    print("想要购买哪件商品?")
    choice = int(input())
    for i in range(len(products)):
        if choice == i:
            print("你选择了第%d件商品\t" % i + "商品信息为:%s\t%d" % (products[i][0], products[i][1]))
            ShoppingChart.append(products[i])
            print("已为您加入购物车~")
            break
        else:
            pass
    print("继续选择.请按任意键       退出.请输入 q ")
    flag = input()
for j in range(len(ShoppingChart)):
    Sum += ShoppingChart[j][1]
    print("%d\t%s\t%d\t" % (j, ShoppingChart[j][0], ShoppingChart[j][1]))
print("您购买的商品总价格为:%d" % Sum)



# 元组tuple   不可修改的数组  （ ）  数据强转  tuple(数据变量名)
# 字典dict     字典变量名.get     若键不存在    返回None     del 删除      字典.clear 清空内容
#   字典.keys()    字典.values()    获取所有键/值      字典.items()  以元组类型获取键值对
# 枚举 enumerate    同时获取列表的下标 和 值      字典1.update（字典2）合并
# 集合set  可变不重复

myList = ['a', 'b', 'c', 'd']
for i, x in enumerate(myList):
    print(i+1, x)
'''

# def 函数/方法    多个返回值 return a,b        外部接收 aa,bb= 函数名
'''
def line():
    print('-'*30)
line()
def lines(i):
    print('-'*i)
i = int(input("请输入横线数量:"))
lines(i)
def Sum(a,b,c):
    print("%d %d %d之和为:%d" % (a, b, c, a+b+c))
    return a+b+c
a = 1
b = 2
c = 3
def avg(sum):
    print("%d %d %d三位数和的平均值为:%f" % (a, b, c, (a+b+c)/3) )
avg(Sum(a, b, c))







