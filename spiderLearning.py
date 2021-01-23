import re
import sys
import urllib.request

import xlwt
import bs4
import sqlite3
import urllib.parse


data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding='utf-8')
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))


response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)      # 返回状态码
print(response.getheaders())

url = "https://passport.ccf.org.cn/sso/login?from=aHR0cHM6Ly9jc3AuY2NmLm9yZy5jbi9jc3Avc2lnbnVwL3NpZ251cF9pbml0LzhhOWUzNzhlNjliN2NhMzIwMTY5YzIxMTNmY2QwMDAwLmFjdGlvbj9fYWNrPTE="
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding='utf-8')
headers = {
    "User-Agent": "Mozilla/5.0 (WindowsNT10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("UTF-8"))
'''
def main():
    url = "https://movie.douban.com/top250?start="

    # askURL(url)
    getData(url)

def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (WindowsNT10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""   # 字符串
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html



def getData(url):
    datalist = []
    for i in range(0, 5):
        URL = url + str(i * 25)
        print("-"*100)
        html = askURL(URL)

    return datalist


if __name__ == '__main__':
    main()
'''

from bs4 import BeautifulSoup

file = open("C:\zhengxin\google.html", "rb")  # rb 读取二进制模式
html = file.read().decode("UTF-8")
bs = BeautifulSoup(html, "html.parser")  # 生成解析BeautifulSoup对象  以树形 层次 结构保存

print(bs.title)  # 打印  第一个  title标签及其内容  ment.Tag
print(bs.title.string)  # ,string 打印  第一个  title标签里的内容  NavigableString
print(bs.img.attrs)  # 以字典(键值对)形式打印 标签里的属性（attributes--------attrs)
print(bs.attrs)
print(bs)   # bs（BeautifulSoup） 类型是document,   即获取的html整个信息文档  属性是空字典 {}
# Comment注释  eg:---新闻---    特殊NavigableString类型 ，打印时不打印注释部分
print(bs.h1.contents)   # 文档的遍历  以列表[]形式打印标签里的内容  ，可用下标访问  contents[1]
# 文档的搜索
# t_list = bs.find_all("a")  # find_all(TAG) 找出html文档中所有tag的内容，以列表[] 形式存储
# print(t_list)


# 正则表达式搜索
T_list = bs.find_all(re.compile("l"))  # 搜索正则表达式规则"l"的所以内容
print(T_list)

# 用方法定义搜索模式 ，用for...in List 逐条打印
print("-"*50)
def id_is_exists(tag):
    return tag.has_attr("id")

List = bs.find_all(id_is_exists)

for item in List:
    print(item)

# 参数形式 搜索    直接在find_all() 中赋值标签的参数   若找class标签参数  class_ = True    //class为类的保留词 故为class_
List = bs.find_all(id="target")
List = bs.find_all(id="target", limit=1)   # 参数limit=？    搜索前n个符合表达式的标签内容
for item in List:
        print(item)

# css选择器
t_list = bs.select('h1')    #按标签查找

t_list = bs.select('.manv')    #  .+类属性值    代表class的属性值

t_list = bs.select('#target')    # #+id标签属性值

t_list = bs.select("a[href]")   # a[属性href]    通过标签a 里的属性值（href）搜索

t_list = bs.select("div > a")   # div  > a > ... 通过子标签逐层搜索 即 <div 标签里的 <a 标签

t_list = bs.select(".manv ~ .bri")   #直接访问与class = manv 同一层次的 class = bri    即兄弟节点
print(t_list[0].get_text())    #获取第一个元素（下标为0）的文本
print(t_list)










