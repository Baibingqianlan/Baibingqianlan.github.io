---
layout: post
title: "djangoproject note 2"
---

## 1. net address ##
using django document on the site[django document](https://docs.djangoproject.com/en/dev/intro/tutorial01/), you can learn more!

## 2. csrf *csrf_token* ##
CSRF（Cross-Site Request Forgery，跨站点伪造请求）是一种网络攻击方式，该攻击可以在受害者毫不知情的情况下以受害者名义伪造请求发送给受攻击站点，从而在未授权的情况下执行在权限保护之下的操作，具有很大的危害性。具体来讲，可以这样理解CSRF攻击：攻击者盗用了你的身份，以你的名义发送恶意请求，对服务器来说这个请求是完全合法的，但是却完成了攻击者所期望的一个操作，比如以你的名义发送邮件、发消息，盗取你的账号，添加系统管理员，甚至于购买商品、虚拟货币转账等。
 [@detail@](http://blog.csdn.net/wjtlht928/article/details/46563809)

## 3. HTTP 请求方式: GET和POST的比较 ##
- GET - 从指定的服务器中获取数据
- POST - 提交数据给指定的服务器处理


> GET方法：
使用GET方法时，查询字符串（键值对）被附加在URL地址后面一起发送到服务器：
`/test/demo_form.jsp?ame1=value1&name2=value2`
特点：
GET请求能够被缓存
GET请求会保存在浏览器的浏览记录中
以GET请求的URL能够保存为浏览器书签
GET请求有长度限制
GET请求主要用以获取数据

> POST方法：
使用POST方法时，查询字符串在POST信息中单独存在，和HTTP请求一起发送到服务器：
POST /test/demo_form.jsp HTTP/1.1
Host: w3schools.com name1=value1&name2=value2
特点：
POST请求不能被缓存下来
POST请求不会保存在浏览器浏览记录中
以POST请求的URL无法保存为浏览器书签
POST请求没有长度限制

[@detail@](https://www.cnblogs.com/igeneral/p/3641574.html )

##  ##