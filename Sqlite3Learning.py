import sqlite3

cnec = sqlite3.connect("test.db")      # 连接数据库 test.db
#conn = sqlite3.connect("movies.db")
print("数据库连接成功~")

c = cnec.cursor()   # cursor 光标所在处
# cc = conn.cursor()

# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''


# sql2 = '''
#     create table movies
#     (id int primary key not null,
#     title text not null,
#     link text not null,
#     bd text not null,
#     inq text not null
#     );
# '''



# 插入数据到sql

# sql2 = '''
#     insert into company(id,name,age,address,salary)
#      values(2,"zhengxin",18,"海口",0)
# '''
#
#
#
# c.execute(sql2)      # 执行操作请求
# #cc.execute(sql2)      # 执行操作请求
# cnec.commit()       # 对象提交数据库的操作


print("成功建表~")

sql3 = "select id,name,address,salary from company"

cursor = c.execute(sql3)

for raw in cursor:
    print("id= ",raw[0])
    print("name= ", raw[1])
    print("address= ", raw[2])
    print("salary= ", raw[3],"\n")

cnec.close()        # 关闭


# 删除  根据id   delete from 表明  where 属性（id）
c.execute("delete from doubanmovies where id = 0")
c.execute("delete from doubanmovies where id = 1")
