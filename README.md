# MVC-web-framework  
## 1.底层使用 Scoket 进行客户端与服务器端的通信，同时实现对 HTTP 协议的接收、解析、生成和返回，并且使用多线程处理并发访问  
## 2.采用基于 MVC 设计模式，实现数据层与显示层解耦，使代码易于维护和重构，提高代码可重用性  
- Model 层：采用基于 PyMySQL 自制 ORM ，并将 MySQL 的增删改查接口封装成一个基类，实现了对不同类型的数据进行实例化形式的数据使用
- View 层：使用 Jinja2 模板，简化页面处理，提升开发效率
- Controller 层：实现了路由注册和接受并解析 HTTP 请求，再通过路由分发生成 HTTP 响应  

## 框架实现的功能  
- 用户的登录和注册
- 用户的权限验证
- Todo 和 Weibo 以及 Weibo 评论的增删改查
- 密码通过 Hash 加盐存储  

# 详细  
## 注册  
![register](https://github.com/FXYGR/MVC-web-framework/blob/master/static/dribbble.gif "注册")
## 登录
![login](https://github.com/FXYGR/MVC-web-framework/blob/master/static/dribbble1.gif "login")
## Todo 增删改查
![todo](https://github.com/FXYGR/MVC-web-framework/blob/master/static/dribbble2.gif "todo")
## Weibo 增删改查
![weibo](https://github.com/FXYGR/MVC-web-framework/blob/master/static/dribbble.gif "weibo")
## 权限验证
![login_required](https://github.com/FXYGR/MVC-web-framework/blob/master/static/dribbble1.gif "login_required")
