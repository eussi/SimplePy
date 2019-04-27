#!/usr/bin/env python
# Author:Wang Xueming

"""定义learning_logs的URL模式"""
from django.conf.urls import url
from .import views  # 句点让Python从当前的urls.py模块所在的文件夹中导入视图

app_name='learning_logs'
urlpatterns = [  # 变量urlpatterns 是一个列表，包含可在应用程序learning_logs 中请求的网页
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]

"""
r'^$' 解析：
    r让Python将接下来的字符串视为原始字符串
    脱字符（^ ）让Python查看字符串的开头
    而美元符号让Python查看字符串的末尾
    总体而言，这个正则表达式让Python查找开头和末尾之间没有任何东西的URL。
    Python忽略项目的基础URL（http://localhost:8000/），因此这个正则表达式与基础URL匹配。
    其他URL都与这个正则表达式不匹配。如果请求的URL不与任何URL模式匹配，Django将返回一个错误页面。

url() 的第二个实参指定了要调用的视图函数。请求的URL与前述正则表达式匹配时，Django将调用views.index 。
    第三个实参将这个URL模式的名称指定为index，让我们能够在代码的其他地方引用它。每当需要提供到这个主页的链接时，
    我们都将使用这个名称，而不编写URL。
    
r'^topics/(?P<topic_id>\d+)/$' 。
    r 让Django将这个字符串视为原始字符串，并指出正则表达式包含在引号内。这个
    表达式的第二部分（/(?P<topic_id>\d+)/ ）与包含在两个斜杠内的整数匹配，并将这个整数存储在一个名为topic_id 的实
    参中。这部分表达式两边的括号捕获URL中的值；?P<topic_id> 将匹配的值存储到topic_id 中；而表达式\d+ 与包含在两个
    斜杆内的任何数字都匹配，不管这个数字为多少位。
"""
