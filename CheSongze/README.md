# 简介

By Che

## 开发环境及涉及框架
### 开发环境
Windows 10 Pro x64, Python v2.7.13, VS Code
### 涉及框架
1. web框架：Flask
2. 爬虫框架：Beautiful Soup 4
## 目录结构
    ├─Task1
    │  ├─1.py       ——通过正则表达式，从test.txt文件中找出所有合法的IP地址
    │  │
    │  ├─2.py       ——实时输出系统当前的CPU/内存/磁盘占用率/网口的实时速率
    │  │
    │  ├─3-4.py     ——在数据库中建表把2.py任务中的实时数据写入数据表，并在上述数据超过限制阈值时报警
    │  │
    │  └─test.txt   ——1.py所用数据
    |
    ├─Task2
    │   ├─1         ——在网页上输出系统当前的CPU/内存/磁盘占用率/网口速率
    │   │
    │   ├─2         ——本地留言系统，无登陆功能
    │   │
    │   ├─3-4       ——本地留言系统，增加了登陆和后台管理功能
    │   │
    │   └─5         ——本地留言系统，在3-4的基础上增加了爬虫功能，
    │               ——默认地址为 http://psnine.com ,并将主要信息输出在该系统的主页
    └─Task3
         ├─1-3      ——后台管理员可以配置规则，在用户发布内容中过滤制指定关键字，
         │     		——并统计各关键字出现次数，后台页面中可以按照其各自出现次数排序。
         │     		——若某关键字被标记为高危，则在出现时会以邮件告警。
         │     		——原邮箱为flasktest@outlook.com, 目标邮箱为j.krma@hotmail.com。
         └─4		——添加聊天室功能。

