<h1 style="text-align: center">绑定公钥</h1>

1.绑定公钥：ssh-keygen -t rsa -C "注册GitHub使用的邮箱@email.com"
<br>
2.进入c盘目录，user内，找到.ssh文件夹，打开id_rsa.pub（vim .ssh/id_rsa.pub）
<br>
3.到github上添加公钥
<br>
4.检查命令：ssh -T git@github.com

<h1 style="text-align: center">网站创建</h1>

一.在桌面新建项目文件夹，比如名为website在命令行里利用 cd 命令进入到 website 文件夹
输入：<br>
1 :python3 -m venv djangoenv
<br>
二.在 website 文件夹内会出现一个 djangoenv 文件夹，然后输入：<br>
1： djangoenv\Scripts\activate
<br>
三.安装后并新建项目：<br>
1: django-admin startproject first .
<br>
2 :django-admin.py startproject first
<br>
四.启动服务
<br>
1:python3 manage.py runserver