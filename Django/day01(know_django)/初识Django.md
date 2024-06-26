# 第一单元 初识Django

## **一、昨日知识点回顾**

```
无
```

------

## **二、本单元教学目标**

### （Ⅰ）重点知识目标

```
1.了解HTTP协议与动态、静态网站的理念
2.独立进行框架项目的创建部署
3.熟悉整个项目框架的目录结构
```

### （Ⅱ）能力目标

```
1.了解HTTP协议与动态、静态网站的理念
2.独立进行框架项目的创建部署
3.熟悉整个项目框架的目录结构
```

------

## **三、本单元知识详讲**

### 1.1  基本概念

#### 1.1.1  http协议

**HTTP 协议**

HTTP 协议是接下来学习网站框架最重要的协议**HTTP** (*HyperText Transfor Protocol*) **超文本传输协议**是互联网目前应用最为广泛的一种协议目前的 **WWW** 服务器都基于 **HTTP** 协议，**HTTP** 协议的目的是为了提供一种发布 **Web** 及接收 **Web 页面数据**的方法**HTTP** 协议常用端口为 **80**，客户端首先通过 **80** 端口向 **HTTP** 服务端发起请求，建立 **TCP** 连接，之后进行 **HTTP** 数据传输

**http和https区别：**

HTTP 传输的数据都是未加密的，也就是明文的，因此使用 HTTP 传输信息非常不安全。为了保证数据能加密传输，网景公司设计了 SSL(Secure Sockets Layer) 协议用于对 HTTP 传输的数据进行加密，从而就诞生了 HTTPS。二者主要区别如下：

1.HTTPS 需要到 ca 申请证书，一般免费证书较少，因而需要一定费用。

2.HTTP 信息是明文传输，HTTPS 则是具有安全性的 ssl 加密传输协议。

3.HTTP 和 HTTPS 连接方式完全不同，端口也不一样，前者是 80，后者是 443。

4.HTTP 的连接很简单，是无状态的。HTTPS 是由 SSL+HTTP 构建的可进行加密传输、身份认证的网络协议，比 HTTP 安全。

![img](https://img-blog.csdnimg.cn/20200829113323236.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM4MTA2OTIz,size_16,color_FFFFFF,t_70)





通过以下趣味图解理解四次挥手：

![img](https://img-blog.csdnimg.cn/20200829121601962.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM4MTA2OTIz,size_16,color_FFFFFF,t_70)





**网络架构**

**HTTP** 协议属于建立在 **TCP** 协议中的应用层上的一种协议，**HTTP** 协议以客户端请求和服务端应答为标准，浏览器(**browser**)通常被人称为客户端，Web 服务器(server)常被称作服务端，所以人们经常称这样浏览器/服务端的架构为 B/S 架构

```python
# B/S 架构
browser /  severice

# C/S 架构
client / serverice 
   软件

# Mysql 分几个端 是什么架构
C/S 架构 
客户端: mysql -uroot -p
Mysql图形化客户端： navicat, DataGrip, pycharm(带的数据库插件) 
    
服务端: mysqld start
pymysql 客户端
```



**短链接**

当浏览器作为客户端访问服务器之后，取到所有所需的数据，立即断开 **TCP** 连接，整个 **HTTP** 连接过程非常短，所以人们也常称 **HTTP** 协议为无连接的协议这也因为每一次 HTTP 的请求，都是重新开启一个新的连接，而不是在一个**历史连接**持续工作，无状态协议

```python
http 协议 规定的内容：

# request对象 -请求报文-- 发请求 要带的内容 规范
请求行-请求头-请求体（get没有）--空行

请求行 request line

请求方式 网址 协议版本 \n\r
 GET    /   HTTP/1.1 \n\r
    
请求头 request header
k:v
host: www.baidu.com
    
请求体 body
k:v
    
空行  \n\r


# response对象 - 响应报文-- 后端 返回给前端的内容 规范
响应行 response line
协议版本 状态码 状态码说明
HTTP/1.1 302  临时重定向
         200  
响应头 response header
k:v
    
空行

响应体 response body (后端返回给前端的数据)
bytes 二进制流--图片流 视频 音频
html  文本
text  纯文本
```



**Request 请求**

当我们使用**HTTP**协议访问某个连接时，首先需要向服务器提交一个***Request***请求

一般当我们使用浏览器访问**Web**服务时，由浏览器完成这个工作，***Request***消息分为三部分，分别包括：***Request Line***、***Request Header***、***Body***

在**linux**下可以通过***curl -V***命令可以查看，当然也可以通过浏览器的检查器看到

```powershell
curl -v https://baidu.com
```

展示的**请求头**是这样的

```powershell
* About to connect() to baidu.com port 80 (#0)
*   Trying 220.181.38.148...
* Connected to baidu.com (220.181.38.148) port 80 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.29.0
> Host: baidu.com
> Accept: */*
>
```

---

**HTTP客户请求的数据格式说明**
HTTP请求包括三部分：请求行(Request Line)，头部（Headers）和实体内容（Body)。其中，请求行由请求方法(method)，请求网址Request-URI和协议 (Protocol)构成，而消息头包括多个属性，实体内容（数据体）则可以被认为是附加在请求之后的文本或二进制文件，只有请求方式为post的时候，实体内容才会有数据（即请求参数）。

```
1、HTTP请求行：请求行格式为Method Request-URI Protocol。在上面这个例子里，“GET / HTTP/1.1”是请求行。
```

常见请求头参数说明：

```
2.Accept:指浏览器或其他客户可以接爱的MIME文件格式。Servlet可以根据它判断并返回适当的文件格式。
3.Accept-Charset：指出浏览器可以接受的字符编码。英文浏览器的默认值是ISO-8859-1.
4.Accept-Language：指出浏览器可以接受的语言种类，如en或en-us，指英语。
5.Accept-Encoding：指出浏览器可以接受的编码方式。编码方式不同于文件格式，它是为了压缩文件并加速文件传递速度。浏览器在接收到Web响应之后先解码，然后再检查文件格式。
6.Authorization：当使用密码机制时用来标识浏览器。
7.Cache-Control：设置关于请求被代理服务器存储的相关选项。一般servlet用不到。
8.Connection：用来告诉服务器是否可以维持固定的HTTP连接。HTTP/1.1使用Keep-Alive为默认值，这样，当浏览器需要多个文件时(比如一个HTML文件和相关的图形文件)，不需要每次都建立连接。
9.Content-Type：用来表名request的内容类型。可以用HttpServletRequest的getContentType()方法取得。
10.Cookie：浏览器用这个属性向服务器发送Cookie。Cookie是在浏览器中寄存的小型数据体，它可以记载和服务器相关的用户信息，也可以用来实现会话功能。
11.Expect：表时客户预期的响应状态。
12.From：给出客户端HTTP请求负责人的email地址。
13.Host：对应网址URL中的Web名称和端口号。
14.If-Match：供PUT方法使用。
15.If-Modified-Since：客户使用这个属性表明它只需要在指定日期之后更改过的网页。因为浏览器可以使用其存储的文件而不必从服务器请求，这样节省了Web资源。由于Servlet是动态生成的网页，一般不需要使用这个属性。
16.If-None-Match：和If-Match相反的操作，供PUT方法使用。
17.If-Unmodified-Since：和If-Match-Since相反。
18.Pragma：这个属性只有一种值，即Pragma：no-cache,表明如果servlet充当代理服务器，即使其有已经存储的网页，也要将请求传递给目的服务器。
19.Proxy-Authorization：代理服务器使用这个属性，Servlet一般用不到。
20.Range：如果客户有部分网页，这个属性可以请求剩余部分。
21.Referer：表明产生请求的网页URL。如比从网页/icconcept/index.jsp中点击一个链接到网页/icwork/search，在向服务器发送的GET/icwork/search中的请求中，Referer是http://hostname:8080/icconcept/index.jsp。这个属性可以用来跟踪Web请求是从什么网站来的。
22.Upgrage：客户通过这个属性设定可以使用与HTTP/1.1不同的协议。
23.User-Agent：是客户浏览器名称。
24.Via：用来记录Web请求经过的代理服务器或Web通道。
25.Warning：用来由客户声明传递或存储(cache)错误。
补充.Transfer-Encoding：
当不能预先确定报文体的长度时，不可能在头中包含Content-Length域来指明报文体长度，此时就需要通过Transfer-Encoding域来确定报文体长度。
通常情况下，Transfer-Encoding域的值应当为chunked,表明采用chunked编码方式来进行报文体的传输。chunked编码是HTTP/1.1 RFC里定义的一种编码方式，因此所有的HTTP/1.1应用都应当支持此方式。
chunked编码的基本方法是将大块数据分解成多块小数据，每块都可以自指定长度
```





**请求方式**

| 请求     | 解释                                           |
| :------- | :--------------------------------------------- |
| **GET**  | 获取服务端数据，比如浏览一个网站，最普通的动作 |
| **POST** | 向服务端提交数据，比如注册帐号的时候           |
| PUT      | 向服务端上传数据                               |
| DELETE   | 删除服务端通过 Request-URL 所标示的资源        |
| TRACE    | 测试服务端是否可以接收到 Request 请求          |
| CONNECT  | 以管道方式连接代理服务器                       |
| OPTIONS  | 返回服务器所支持的其他 HTTP 请求方法           |
| HEAD     | 与 GET 方法类似，但不返回服务器响应时的消息体  |


---

**Response 响应**

服务器接收到之后，会向我们返回一个***Response***响应，浏览器接收到了***Response***之后，会帮助我们对信息进行解析，之后我们就可以看到对应的**Web**页面及获取到的资源

同样也可以使用命令或者浏览器检查查看得到效果

```powershell
curl -v https://baidu.com
```

效果是这样的

```powershell
< HTTP/1.1 302 Moved Temporarily
< Server: bfe/1.0.8.18
< Date: Thu, 19 Nov 2020 01:45:26 GMT
< Content-Type: text/html
< Content-Length: 161
< Connection: keep-alive
< Location: http://www.baidu.com/
< 
<html>
<head><title>302 Found</title></head>
<body bgcolor="white">
<center><h1>302 Found</h1></center>
<hr><center>bfe/1.0.8.18</center>
</body>
</html> 
```

**状态码**

| **状态码** | **状态码英文标示**            | **意义**                                                     |
| :--------- | :---------------------------- | :----------------------------------------------------------- |
| 100        | Continue                      | HTTP/1.1 中新增状态码，表示客户端可以继续请求 HTTP 服务器    |
| 101        | Switching Protocols           | 服务端切换请求协议，切换到 HTTP 协议新版本                   |
| **200**    | OK                            | 客户端的请求服务端正常完成                                   |
| **301**    | Moved Permanently             | 客户端请求的资源已被永久移动到新的 URL                       |
| **302**    | Found                         | 客户顿请求的资源被临时移动，客户端继续使用原有 URL；常用于三方登录之后的跳转 |
| 304        | Not Modified                  | 请求的资源未被修改，可以继续访问原 URL<br>常用于使用缓存的情况下 |
| 400        | Bad Request                   | 客户端的请求语法错误，或无法解析请求                         |
| 401        | Unauthorized                  | 请求需要经过身份验证                                         |
| 402        | Payment Required              | 保留状态码，为以后使用做准备的呢                             |
| 403        | Forbidden                     | 服务端直接拒绝客户端的请求                                   |
| **404**    | Not Found                     | 客户端请求的资源找不到                                       |
| 405        | Method Not Allowed            | 客户端请求的方式不被允许                                     |
| 406        | Not Acceptable                | 客户端请求的内容无法正常完成                                 |
| 499        | Client has closed Connection  | 服务端处理该请求花费了太长的时间                             |
| 500        | Internal Server Error         | 服务端内部错误；可能是因为 Web 服务配置文件读取错误，也可能是因为用户权限等等问题导致 |
| **502**    | Bad Geteway                   | 服务端内部错误，服务端错误的网关                             |
| 503        | Service Unavailable           | 服务端无法响应客户端的请求；                                 |
| 504        | Gateway Time-out              | 服务端处理请求超时，或者可能是访问的网管超时                 |
| 505        | HTTP Version not<br>Supported | 客户端请求的 HTTP 协议版本无法被服务端支持，<br>可能是你的浏览器太古老了 |

#### 1.1.2  动态、静态网站

**静态网站**

某一天，你的老板让你开发一款新闻站点，你有什么办法呢？

学过***html***的同学可以知道，我可以把新闻写在***html***页面中，并加上美丽的***css***样式，绚丽的***js***动画效果。

但是我们要考虑一个问题，新闻每一天都是不停变化的，那么怎么能快速迅捷的将每一天崭新的内容快速的发布在网页中，让我们的阅读者可以及时的看到新鲜的内容呢？

这很明显是一项需要**拼手速**的工作，而最初这些拼手速所写成的网站，也叫做**静态网站**

所谓**静态网站**的概念也很简单，就是将数据直接写死在页面中，静态网站也因此经常使用在一些数据不经常改变的场景下，网站内容也是相当的稳定，几乎不会怎么更新

比如一些成型的**美女图片网站**、**公司企业的官网**


---

**动态网站**

那么如何解决这样新闻站点每天海量的数据更新呢？这很明显是一项是通过手动修改页面不实际的任务。

于是乎，久而久之，人们发现我们其实展示数据的页面都是类似的，只是每一个位置上每一天的内容不一样，那么可以提前在这些位置挖一些**坑**，数据不再是写死的，而是通过数据库等手段传递到这些**坑位上**，而负责传递数据的这个部分，我们一般就叫做***Web 框架***

这也是我们接下来要学习的***Django***框架他的主要意义，为**页面传递数据**，或者**接受页面数据**再**传递给数据库**或做一些其他操作

再详细些，那么就是获取用户的请求之后，进行一系列的操作处理，再为用户返回数据，并渲染到页面上


---

**一次用户的访问，由两部分组合，发起*Request*请求，由框架返回*Response***

---

### 1.2 Django框架

```python 
  def app(environ, start_response): 
        start_response('200 OK', [('Content-Type', 'text/plain')]) 
        yield "Hello world!\n"
    
    body = []    status_headers = []    
    def start_response(status, headers): 
        status_headers = [status, headers]        
        return body.append(status_headers) 
    
   app_iter = app(environ, start_response)    
            try:        
                 for item in app_iter:           
                body.append(item)    
            finally:        
                    if hasattr(app_iter, 'close'):            
                        app_iter.close()    
                        return status_headers[0], 
                    
                    
                    
status_headers[1], ''.join(body)status, headers, body = call_application(app, {...environ...})
```



#### 1.2.1  框架介绍

**MVC 架构模式**

MVC是最早的设计模式，也是使用最广的设计模式

特点：高内聚、低耦合

***M-model***：**数据模型**，和**MVT**的 m 是一样的，同样用来操作数据库

***V-view***：**视图**，和**MVT**的 T 是一样的，用来进行数据的可视化

***C-Controller***：**控制器**，相当于**MVT**中的 C，用来进行数据的逻辑操作

```python
#  MVC 的交互流程
1. 前端 View视图里面页面--发送请求 给后台后端
2. 控制器来接收请求Controller----> 处理主业务逻辑（1.判断路由 2.解析参数 3.对接Model 4.返回数据）
3. Model-交互数据库-返回数据给 C 
4. C把数据 传给V 展示
```

**MVT  架构模式**

***Django***主要采用**MVT**模式

***M-model***：**模型**，操作数据库功能部分

***V-View***：**视图**，处理业务逻辑的位置，提取数据、获取用户数据等等操作都在这里

***T-Template***：**模版**，用来展示视图操作后的数据渲染到html上，也可以在模版中为用户**提供表单**，让用户可以提交数据


---


| MVT              | MVC                |
| :--------------- | :----------------- |
| ***M-model***    | ***M-model***      |
| ***V-View***     | ***C-Controller*** |
| ***T-Template*** | ***V-view***       |

```python
#  MVT 的交互流程 --前后端不分离开发， 后台工程师 会写前端代码（所有的， 只写模板部分）
#  MVC            前后端分离， 后台工程师 只写后台代码--json数据
1. 发请求----django框架--V--处理主业务逻辑（1.判断路由 2.解析参数 3.对接Model 4.返回数据）
2. V--获取数据--Model(交互数据库)
3. model--->V
4. V-->数据---Template-模板
5. Template--模板-数据渲染---展示

```

---

**Django 介绍**

***Django***是一个开放源代码的**Web 应用框架**，由纯***Python***写成，是目前 Python 语言中主流  三大**Web**框架之一(***flask***、***django***、***tornado***、**fastapi**)，是最容易上手的框架

***Django***最初是被开发来用于管理劳伦斯出版集团旗下的一些以新闻内容为主的网站的，即是**CMS(**内容管理系统**)**软件

框架是以比利时的吉普赛爵士吉他手***Django Reinhardt***来命名的，这也代表着这是一门及其优雅的框架


---


* 那啥又是**CMS**(***Content Management System***)呢？

其实说白了，这就是一个管理内容的平台，可以让用户、企业对自己的资源进行便捷的展示、修改、删除等操作


---


* 那***Django***有哪些应用呢？

***Pinterest***：这是世界上最大的图片社交分享网站，在这个网站，你可以创建和管理主题图片集合，例如事件、兴趣和爱好。2009 年就开始建设，目前拥有超过三亿用户，并且绝大多数用户都是女性

![图片](images/WFRUNFp5mzpBhRG1.png!thumbnail)

***bitbucket***：这是一家源代码托管网站，拥有无限制的私人仓库个数，磁盘空间，以及灵活的权限控制等

![图片](images/sfh2d9MjH1lvpmC9.png!thumbnail)

***nasa***：美国宇航局官方站点

![图片](images/eI3yyF3SK07LkJ6g.png!thumbnail)

国内还有比较知名的豆瓣网，也是用 Django 的哦


---


* ***Django***的特点:

  ```python
  1. 重量级的框架 --包含很多现成功能(用户认证-发邮件-模型类-ORM框架)
  2. 大而全
  3. 速度慢--相对于轻量级（flask, fastapi, tornado）
  4. 在django3.0 之前 它是同步的， 之后 支持异步的
  5. django-admin 后台管理系统
  适用场景： 项目比较大， 适用django比较健全 ，后期好维护 和扩展
           快速开发。  功能多， 很多都是现成 
  ```
  

总结来说，***Django***适合与内容有关的项目，常见的就是后台管理，一些系统，这个框架适合**敏捷开发**，可以让开发者快速高效的产出，而其他需要并发等的业务体系，***Django***就不太适合了

#### 1.2.2  框架安装

```python
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple  # 设置清华镜像 

pip install django==4.2.2  -i https://pypi.tuna.tsinghua.edu.cn/simple  # 安装django
```



#### 1.2.3  项目创建

```python
# 1. 终端指令 创建 django 项目--myproject
django-admin startproject myproject

# 2. 进入到项目 里面
cd myproject

```

通过启动***Django***自带的开发服务器，我们可以很快速的启动当前创建好的空壳项目，并且看到来自***Django***的友好提示

```powershell
# 3. 启动 django 服务的指令
python manage.py runserver
```

#### 1.2.4  目录介绍

创建好一款***Django***项目之后，它已经是具备了一些基本的文件及文件夹

* ***manage.py***：用来管理当前项目的一个命令行工具
* ***myproject***：项目**主文件夹**，包含了项目最基本的配置文件及路由文件
    * *`__init__.py`*：空文件，用来指明当前的***myproject***为一个可导入的模块包
    * *settings.py*：项目主要配置文件
    * *urls.py*：项目主要路由配置文件
    * *wsgi.py*：项目部署**WSGI**并发服务器时所需要的配置文件

**settings.py 配置**

这个文件包含了诸多未来我们会操作的***Django***配置，其中默认提供的选项解释如下

* ***BASE_DIR***：当前项目工作目录，用来在每一次开启项目时动态找到这个项目运行在当前操作系统下的哪个目录下
* ***SECRET_KEY***：加密的***hash***值以及保护某些签名数据的关键密钥
* ***DEBUG***：**调试模式**，在这个模式下，你可以很清晰的看到出错信息，如果关闭了，那么出错将会变为状态码或者**隐蔽性**更高的报错页面
* ***ALLOWED_HOSTS***：当前主机所拥有的**IP**哪些可以被外界使用访问***Django***
* ***INSTALL_APPS***：***Django***项目中所有使用的应用名称，自创建子应用也要加到这里，不然**ORM**数据库无法被识别到
* ***MIDDLEWARE***：中间件，用来在 请求***request***和 响应***reponse***过程中添加功能，比如确保安全性，传输保存***Session***等
* ***ROOT_URLCONF***：主路由配置文件，字符串填写 url.py 文件路径
* ***TEMPLATES***：模板文件配置项
* ***WSGI_APPLICATION***：WSGI 服务器配置项，找到当前 django 下的 wsgi 引入 APP 文件
* ***DATABASES***：数据库配置项，默认使用**SQLite3**，一个**本地文件数据库**
* ***AUTH_PASSWORD_VALIDATORS***：检查用户密码强度的验证程序列表，不过是针对***admin***组件下的用户，而非自定义
* ***LANGUAGE_CODE***：所使用语言文件，一般国内项目采用***zh-Hans***
* ***TIME_ZONE***：所使用时区，一般国内项目采用***Asia/Shanghai***
* ***USE_I18N***：国际化支持 18 表示 Internationalization 这个单词首字母 I 和结尾字母 N 之间的字母有 18 个
* ***USE_L10N***：是*localization*的缩写形式，意即在 l 和 n 之间有 10 个字母
* ***USE_TZ***：开启了*Time Zone*功能，则所有的存储和内部处理，包括 print 显示的时间将是是 UTC 时间格式
* ***STATIC_URL****：*访问静态资源时的*URL***路径

### 1.3  **子应用**

#### 1.3.1  子应用是什么及其意义

**应用**是一个专门**做某件事**的网络应用程序，比如博客系统中的用户功能部分，一个考试系统中管理试卷的部分。

**项目**则是一个网站使用的配置和**应用**的**集合**，一个项目可以包含很多个**app** **应用**，**应用**可以被很多个项目使用。

| 用户部分 APP                                                 | 帖子部分 APP                                             |
| :----------------------------------------------------------- | :------------------------------------------------------- |
| **用户登录**、**用户注册**，**用户密码找回**，**用户**个人资料管理 | 帖子发布、帖子评论、帖子编辑、帖子点赞点踩、帖子热度排名 |


---

子应用:  通过文件夹封装 同类型的小功能， 封装思想

#### 1.3.2  子应用创建

```python
python manage.py startapp appname
django-admin startapp appname
```

#### 1.3.3 子应用的注册

```python
# settings.py 
INSTALLED_APPS = [
    
    'appname',
]
```



#### 1.3.3  子应用目录结构

-   *app/*：app目录
    -   *admin.py*：这个**app**所使用表模型在admin注册展示时需要的文件
    -   *views.py*：视图函数文件，编写主要的增删改查等数据逻辑的地方
    -   *models.py*：未来操作数据库时，如果使用**ORM**映射关系，那么将使用该文件

#### 1.3.4  子应用视图逻辑

创建好了子应用，接着来编写实际的功能视图函数吧，让我们具有一个自己真正的页面！


---

**编写视图**

打开*app***下的*views.py***文件，编写视图函数

```python
from django.http import HttpResponse
def index(request):
return HttpResponse("<h1>Hello world</h1>")
```

在views.py中我们通过编写函数的形式，接收用户请求的request**并返回一个*response***，这个***response****通过***HttpResponse方法进行返回，这个方法很简单，返回的就是一个*html*字符串

---

**编写路由**

视图好比我们在超市摆放的一件件商品，可以为顾客提供服务，那么想让顾客真正可以购买得到这件商品，我们还需要给用户提供一个地图，或者说一个指引，这个指引就是浏览器中我们常输入的一段*URL***连接地址

接下来就需要把视图方法对应到一个固定唯一的*URL***地址上，让用户可以通过这个地址，访问到这个视图

打开项目主目录下的*urls.py***文件，编写路由映射

```python
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
path('admin/', admin.site.urls), #admin 控制界面路由
path('',views.index)
]
```

访问一个页面其实就是通过一个*URL*连接地址找到了服务器上的一个视图函数，**path**函数用来处理一个路由对应的视图映射

```python
path(route, view, name)
'''
route： 匹配规则，是一个字符串
view：对应的视图函数
'''
```



### 1.4  **模版页面**

#### 1.4.1  模版页面返回

现在再来思考一下，只是简单的返回一个html字符串，我们可以满足吗？难道平时的网站就这么朴素吗？

那当然是不行的，返回一个字符串这也太low了，也不好看，那么现在就来返回一个正式HTML页面吧！

**模版配置**

首先要告诉Django，你准备把接下来的html页面存放在哪里，那么需要打开settings.py文件，找到TEMPLATES选项，修改其中的DIRS属性，在这里添加我们的html文件夹位置

```python
# project.settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

一般我们会把存放**HTML**的文件夹名字命名为*template*，翻译过来就叫做**模版文件**，至于为啥叫模版，我们稍后来揭晓

**创建模版**

有了这个文件夹的配置之后，接下来在项目根目录下创建与配置同名的文件夹*template/*

并在其中书写一个简单的*html*，并命名为***index.html***

```xml
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hi</title>
</head>
<body>
<h1>真不错</h1>
<p>
    今天这个天气是<strong>晴天</strong>
</p>
</body>
</html>
    
```

#### 1.4.2 Template的配置流程

```python
#  1. 项目根目录 创建 templates 文件夹

#  2.在settings.py--配置模板路径

#  3. templates 文件夹下面 创建 .html
```

**视图渲染**

有了*html*，目录也配置好了，那么紧接着就是让视图去返回这个文件，那么现在我们要引入一个新的方法叫做***render***，这个方法专门用来返回一个*html*页面，并且在未来，我们还会了解到这个方法的更高级用处，就是传递上下文**模版变量**

修改app下的视图方法，返回这个页面，页面路径不需要绝对路径，使用*template/*下的相对路径即可

```python
# app.views.py
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
```



---

## **四、本单元知识总结**

```
1.了解HTTP协议与动态、静态网站的理念
2.独立进行框架项目的创建部署
3.熟悉整个项目框架的目录结构
```

