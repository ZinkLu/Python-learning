# Django框架

[toc]

## 1. Django介绍

### 1.1 简介

- `Django`，是用`python`语言写的开源web开发框架，并遵循MVC设计

- 劳伦斯出版集团为了开发以新闻内容为主的网站，而开发出来了这个框架，于2005年7月在BSD许可证下发布

- 这个名称来源于比利时的爵士音乐家`DjangoReinhardt`，他是一个吉普赛人，主要以演奏吉它为主，还演奏过小提琴等

- 由于Django在近年来的迅速发展，应用越来越广泛，被著名IT开发杂志SDTimes评选为2013SDTimes100，位列"API、库和框架"分类第6位，被认为是该领域的佼佼者

- Django的主要目的是简便、快速的开发数据库驱动的网站

- 它强调代码复用，多个组件可以很方便的以"插件"形式服务于整个框架，Django有许多功能强大的第三方插件，你甚至可以很方便的开发出自己的工具包。这使得Django具有很强的可扩展性。它还强调快速开发和DRY(DoNotRepeatYourself)原则

<br>

### 1.2 特点

#### 1.2.1 重量级框架

- 对比Flask框架, Django原生提供了众多的功能组件, 让开发更加简便快速:

    - 动化脚本工具

    - 数据库ORM支持

    - 模板

    - 表单

    - Admin管理站点

    - 文件管理

    - 认证权限

    - session机制

    - 缓存

#### 1.2.2 MVT模式

- `MVC`模式: 其核心思想是分工, 解耦, 让不同的代码之间降低耦合, 增强代码的可拓展性和可一致性, 实现向后兼容

    - `M`: `Model`主要封装对数据库层的访问, 对数据库中的数据进行增删改查

    - `V`: `View`用于封装结果, 生成页面展示的`html`内容

    - `C`: `Controller`, 用于接受请求, 处理业务逻辑, 与`Model`和`View`交互, 返回结果

- `Django`中的`MVT`

    - `M`: `Model`, 与`MVC`中的`M`功能相同, 负责和数据库的交互, 进行数据处理

    - `V`: `View`, 与`MVC`中的`C`功能相同, 接受请求, 进行业务处理, 返回应答.

    - `T`: `Template`, 与`MVC`中的`V`功能相同, 负责封装构造返回的HTML

<br>
<br>
<br>

## 2. 工程搭建

### 2.1 创建工程

#### 2.1.1 创建

- 在`Django`中, 项目工程可以使用命令来创建

    ```sh
    django-admin startproject 工程名称
    ```

#### 2.1.2 工程目录说明

- 创建完以后的目录如下

    ```
    .
    ├── DjangoLearning
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
    ```

- 目录结构说明
    
    - `setting.py`是项目的整体配置文件

    - `urls.py`是项目的URL配置文件

    - `wsgi.py`是项目与WSGI兼容的Web服务器入口

    - `manage.py`是项目管理文件, 通过它管理项目

#### 2.1.3 运行开发服务器

- `Django`实现了一个测试服务器, 只能在开发阶段测试使用

    ```sh
    python manage.py runserver host:port
    ```

    > 默认的地址为`127.0.0.1:8000`

<br>

### 2.2 创建子应用

在Web应用中, 通常有一些业务功能模块是在不同的项目中都可以复用的, 故在开发中通常将工程项目拆分为不同的子功能模块, 各功能模块间可以保持相对的独立, 在其他工程项目中需要用到某个特定的功能模块时, 可以将该模块代码整体复制过去, 达到复用.

> 在Flask框架中也有类似子功能应用模块的概念 -- Blueprint 蓝图

**而Django的视图编写是放在子应用中的**

#### 2.2.1 创建子应用

- 同样, 可以使用命令创建新的子应用

    ```sh
    python manage.py startapp 子应用名称
    ```

#### 2.2.2 子应用目录说明

- 创建完以后目录如下:

    ```
    .
    ├── DjangoLearning
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   └── settings.cpython-37.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── users
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py
    ```

- 目录结构说明

    - `admin.py`文件跟网站的后台管理站点配置相关

    - `apps.py`文件用于配置当前子应用的相关信息

    - `migrations`目录用于存放数据库迁移历史文件

    - `models.py`文件用于保存数据库的模型类

    - `tests.py`文件用于开发测试用例, 编写单元测试

    - `views.py`文件用于编写Web应用视图

#### 2.2.3 注册/安装 子应用

- 创建出来的子应用需要安装后才能使用(Django的设计哲学之: 及插即用)

- 在功能配置文件`setting.py`中, `INSTALLED_APPS`保存了工程中已经注册安装的子应用, 初始工程中的`INSTALLED_APPS`如下:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

- **安装一个子应用, 将子应用的配置信息文件apps.py中的AppConfig类添加到 `INSTALLED_APPS` 列表中**

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'users.apps.UsersConfig'
    ]
    ```

<br>

### 2.3 创建视图

- `Django`中的视图定义在子应用的`views.py`中

#### 2.3.1 创建

- 打开users模块, 在`views.py`中编写视图代码

    ```python
    from django.http import HttpResponse

    def index(request):
        """
        index视图
        :param request: 包含了请求信息的请求对象
        :return: 响应对象
        """
        return HttpResponse("hello world~")
    ```

- 说明:

    - 视图函数的第一个传入参数必须定义, 用于接收Django构造的包含了请求数据的`HttpRequest`对象, 通常名为`request`

    - 视图函数的返回值必须为一个响应对象, 不能像`Flask`一样直接返回一个字符串, 可以将要返回的字符串数据放到一个`HttpResponse`对象中

#### 2.3.2 定义路由URL

1. 在子应用中新建一个`urls.py`文件用于保存该应用的路由

2. 在该文件中定义路由信息

    ```python
    from django.conf.urls import url
    from . import views

    # urlpatterns是被Django自动识别的路由列表变量
    urlpatterns = [
        # 每个路由信息都要使用url函数来构造
        # url(路径, 视图)

        url(r"^index/$", views.index)
    ]
    ```

3. 在工程目录下的`url.py`添加子应用的路由数据

    ```python
    from django.conf.urls import url, include
    from django.contrib import admin

    urlpatterns = [
        url("", admin.site.urls), # django默认

        # 添加
        url(r"users/", include("users.urls"))
    ]
    ```

    - 使用`include()`来将子应用users例的全部路由包含进工程路由中

    - `r"users/"`决定了users子应用的**所有**路由都以`/users/`开头, 刚才视图函数完整的url为`/users/index`

    - `include()`不仅可以传递字符串, 还可以直接传递应用的urls模块

    ```python
    from django.conf.urls import url, include
    from django.contrib import admin
    import users.urls  # 先导入应用的urls模块

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        # url(r'^users/', include('users.urls')),
        url(r'^users/', include(users.urls)),  # 添加应用的路由
    ]
    ```

4. 启动

    ```sh
    python manage.py runserver
    ```

<br>
<br>
<br>

## 3. 配置文件, 静态文件, 路由

### 3.1 配置文件

#### 3.1.1 BASE_DIR

- 当前工程的的根目录, Django会依此来定位工程内的相关文件

    ```python
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ```

#### 3.1.2 DEBUG

- 调试模式, 创建工程后初始值为`True`, 即默认工作在天使模式下

- 作用:

    - 修改代码文件, 程序自动重启

    - Django程序出现异常时, 向前端显示详细的错误追踪信息(非调试下返回500)

    > 注意生产环境下必须关闭DEBUG

#### 3.1.3 本地语言与市区

- Django支持本地化处理, 即显示语言与时区

- 本地化将显示的语言, 时间等使用本地的习惯, 将语言设置为**简体中文**, 时区设置为**上海**

    ```python
    LANGUAGE_CODE = 'zh-hans'
    TIME_ZONE = 'Asia/Shanghai'
    ```

<br>

### 3.2 静态文件

Django中提供了一种解析的方式配置静态文件路径。静态文件可以放在项目根目录下，也可以放在应用的目录下，由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下，方便管理。

- 为了配置静态文件, 需要配置两个参数:

    - `STATICFILES_DIRS` 存放查找静态文件的目录

    - `STATIC_URL` 访问静态文件的URL前缀

1. 配置示例

    1. 在项目根目录下创建`static_files`目录来保存静态文件

    2. 在`setting.py`中修改静态文件的两个参数为

    ```python
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static_files"),
    ]
    ```

    3. 此时在`static_files`添加的任何静态文件都可以使用网址`/static/`去访问了

> 注意:
>
> Django仅在调试模式下能对外提供静态文件
>
> 当在生产模式下时, Django不再对外提供静态文件, 需要用`collectstatic`命令来收集静态文件并交由其他静态文件服务器来提供

<br>

### 3.3 路由说明

#### 3.3.1 路由定义位置

- Django的主要路由信息定义在工程同名目录下的`urls.py`文件中, 该文件是Django解析路由的入口

- 每个子应用为了保持独立, 可以在各个子应用中定义属于自己的`urls.py`来保存该应用的路由. 然后用主路由文件包含各应用的子路由的数据

#### 3.3.2 路由解析顺序

- Django在接受到一个请求时, 从主路由文件中的`urlpatterns`列表中以由上至下的顺序查找对应路由规则, 如果发现规则为`include`包含, 则在进入被包含的`urls`中的`urlpatterns`列表由上至下进行查询.

- 值得关注的**由上至下**的查找顺序, 有可能会使上面的路由屏蔽掉下面的路由, 带来非预期的结果

    ```python
    urlpatterns = [
        url(r"^say", views.say),
        url(r"sayhello", views.sayhello),
    ]
    ```

    - 即使访问`/sayhello/`路径, 预期应该进入sayhello视图函数执行, 但实际优先查找到了say路由规则, 由于也符合匹配规则, 只会执行say视图函数

> 需要注意定义路由的顺序, 避免出现屏蔽效应

#### 3.3.3 路由命名与reverse反解析(逆向)

1. 路由命名

    - 在定义路由的时候, 可以为路由命名, 方便查找特定视图的具体路径信息

    ```python
    # 比如在使用include函数定义路由时, 可以使用namespace 参数定义路由的命名空间
    url(r"^users/", include("users.urls", namespace="users")),
    ```

    - 命名空间表示, 凡是users.urls中定义的路由, 均属于namespace指明的users名下

    - 命名空间的作用: **避免不同应用中的路由使用了相同的名字发生冲突, 使用命名空间区别开**

    ```python
    # 在定义普通路由时, 可以使用name参数指明路由的名字
    urlpatterns = [
        url(r"^index/$", views.index, name="index"),
        url(r"^say", views.say, name="say"),
    ]
    ```

    > 这里有默认值么?

2. reverse反解析

    - 使用reverse函数, 可以根据路由名称, 返回具体的路径

    ```python
    from django.urls import reverse 

    def index(request):
        return HttpResponse("hello the world!")

    def say(request):
        url = reverse("users:index")  # 返回 /users/index/
        print(url)
        return HttpResponse("say")
    ```

    - 对于未指明`namespace`的, `reverse(name)`

    - 对于指明`namespace`的, `reverse(namespace:name)`

<br>

### 3.4 路径结尾/的说明

- Django中定义路由时, 通常以`/`结尾, 其好处是用户访问不以`/`结尾的相同路径时, Django会把用户重定向到以`/`结尾的路径上, 而不会返回404

    ```python
    urlpatterns = [
        url(r"^index/$", views.index, name="index")
    ]
    ```

    - `index`和`index/`都能访问

    > 虽然路由结尾带`/`能带来好处, 但是却违背了HTTP中URL表示资源位置路径的设计理念

<br>
<br>
<br>

## 4. 请求与响应

### 4.1 请求Request

- 利用HTTP协议向服务器传递参数的途径:
    
    1. 提取URL特定部分(动态URL)

    2. 查询字符串

    3. 请求体(body)中发送的数据(POST) 比如表单, json, xml

    4. 在HTTP报文头(header)中 cookie

#### 4.1.1 URL路径参数

- 在定义路由URL时, 可以使用正则表达式提取参数的的方法从URL中请求参数, Django会将提取的参数直接传递到视图的参数中

    - 未命名参数按定义顺序传递

    ```python
    url(r"^weather/([a-z]+)/\d{4}/$", views.weather)

    def weather(request, city, year):
        print("city=%s" % city)
        print("year=%s" % year)
        return HttpResponse("OK")
    ```

    - 命名参数按名字传入

    ```python
    # 这里使用的命名参数是根据正则表达式中的命名分组来确定的
    url(r"^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$", views.weather)

    def weather(request, year, city):
        print("city=%s" % city)
        print("year=%s" % year)
        return HttpResponse("OK")
    ```

#### 4.1.2 Django中的QueryDict对象

- 在`HttpRequest`对象的属性`GET`, `POST`都是`QueryDict`类型的对象

- 与`Dict`不同, `QueryDict`类型的对象用来处理同一个键带有多个值的情况

    - `.get()`根据键获取值
    
        - 如果一个键同时有多个值将获取最后一个值

        - 如果键不存在则返回None值, 可以设置默认值
    
    - `.getlist()`根据键获取值, 值以列表返回

        - 如果键不存在则返回空列表, 可以设置默认值

#### 4.1.3 查询字符串QueryString

- 获取请求路径中的查询字符串参数, 可以通过`request.GET`属性获取, 返回`QueryDict`对象

    ```python
    # /qs/?a=1&b=2&a=3

    def qs(request):
        a = request.GET.get("a")
        b = request.GET.get("b")
        alist = request.GET.getlist("a")
        print(a) # 3
        print(b) # 2
        print(alist) # ["1", "3"]
        return HttpResponse("OK")
    ```

    - **即使客户端使用POST请求, 依然可以通过`request.GET`获取请求中的查询字符串数据**

#### 4.1.4 请求体 - body

请求体数据格式不固定, 可以是表单类型字符串, 可以是JSON字符串, 可以使XML字符串, 应该区别对待.

- **POST**, **PUT**, **PATCH**, **DELETE** 都可以发送请求体

1. 表单类型数据 - Form Data

    - 可以通过`request.POST`属性获取, 也是`QueryDict`对象
        
    - `request.POST`只能用来获取POST方法的请求体**表单数据**

2. 非表单数据 - Non-Form Data

    - 非表单类型的请求体数据, Django无法自动解析, 可以通过`request.body`属性获取原始的请求数据, 按照对应的格式去进行处理. 需要注意`request.body`返回`bytes`类型

    ```python
    # JSON数据 {"a":1, "b":2}
    import json
    def get_body_json(request):
        json_str = request.body
        json_str = json_str.decode()  # python3.6 无序执行这一步
        req_data - json.loads(json_str)
        print(req_data["a"])
        print(req_data["b"])
        return HttpResponse("OK")
    ```

> PS: Django默认开启了CSRF保护, 可以将setting.py中的中间件csrf注释掉

#### 4.1.5 请求头 - headers

- 通过`request.META`获取请求头中的数据, `Dict`类型

- 看源码得知, 这里的`request.META`就是WSGI服务器传给web应用的`environ`参数, 包含了请求环境的所有信息, 也包括了WSGI服务器相关信息

常见的请求头有:

- `CONTENT_LENGTH` – 请求体的字符串长度.

- `CONTENT_TYPE` – 请求体中的文件类型.

- `HTTP_ACCEPT` – 可接受的响应类型.

- `HTTP_ACCEPT_ENCODING` – 可接受的编码方式.

- `HTTP_ACCEPT_LANGUAGE` – 可接受的语言.

- `HTTP_HOST` – HOST地址.

- `HTTP_REFERER` – The referring page, if any.

- `HTTP_USER_AGENT` – The client’s user-agent string.

- `QUERY_STRING` – The query string, as a single (unparsed) string.

- `REMOTE_ADDR` – The IP address of the client.

- `REMOTE_HOST` – The hostname of the client.

- `REMOTE_USER` – The user authenticated by the Web server, if any.

- `REQUEST_METHOD` – A string such as "GET" or "POST".

- `SERVER_NAME` – The hostname of the server.

- `SERVER_PORT` – The port of the server (as a string).

#### 4.1.6 其他常用HttpRequest对象属性

- `method`: 请求方法 字符串

- `user`: 请求的用户对象

- `path`: 表示请求的页面完整路径, 不包含域名

- `encoding`: 提交数据的编码方式:

    - `None`的话表示使用浏览器的默认设置, 一般为`utf-8`

    - 这个属性是可写的, 可以通过修改它来访问表单数据使用的编码, 接下来所有的数据都用这种编码方式

- `FILES`: 一个类似于字典的对象, 包含所有的上传文件

<br>

### 4.2 响应Response

视图在接受请求后, 必须返回`HttpResponse`对象或者子对象

#### 4.2.1 HttpResponse

- 使用`django.http.HttpResponse`来构造响应对象

    ```python
    HttpResponse(content=响应体, content_type=响应体数据类型, status= 状态码)
    ```

- 也可以通过`HttpResponse`对象属性来设置响应体, 状态码

    - `content`: 表示返回的内容

    - `status_code`: 返回的HTTP响应状态码

- 响应头可以直接将`HttpResponse`对象当做字典进行响应头键值对的设置

    ```python
    response = HttpResponse()
    response["Content-Type"] = "text/html"
    ```

#### 4.2.2 HttpResponse子类

Django提供一系列HttpResponse子类, 可以快速设置状态码

- HttpResponseRedirect 301

- HttpResponsePermanentRedirect 302

- HttpResponseNotModified 304

- HttpResponseBadRequest 400

- HttpResponseNotFound 404

- HttpResponseForbidden 403

- HttpResponseNotAllowed 405

- HttpResponseGone 410

- HttpResponseServerError 500

#### 4.2.3 JsonResponse

- 如果想返回JSON数据, 可以使用`JsonResponse`来构造响应对象
    
    - 自动转化成JSON字符串

    - 设置响应头Content-Type为application/json

    ```python
    from django.http import JsonResponse

    def demo_view(request):
        return JsonResponse({"city":"beijing", "subject":"python"})
    ```

    - `JsonResponse`默认只支持传入`dict`类型的数据, 如果想返回已经处理好的字符串, 需要传入参数`safe=False`

#### 4.2.4 redirect重定向

- 在Django中, 有一种重定向的捷径

    ```python
    from django.shortcuts import redirect

    def demo_views(request):
        return redirect("/index.html")
    ```

<br>

### 4.3 Cookie

#### 4.3.1 设置Cookie

- 可以通过`HttpResponse`对象中的`.set_cookie()`方法来设置cookie

    ```python
    HttpResponse().set_cookie("cookieName", value="cookieValue", max_age=0)
    ```
    
    - `max_age`单位为秒, 默认为None, 如果是临时cookie, 可以将`max_age`设置为None

#### 4.3.2 读取cookie

- 可以通过`HttpRequest`对象的`COOKIES`属性来读取本次请求携带的cookie值

- `request.COOKIES`为`dict`类型

<br>

### 4.4 Session

#### 4.4.1 启用Session

- Django项目默认启用Session

- 如果不需要使用Session可以到`setting.py`中的`MIDDLEWARE`的`SessionMiddleware`注释掉

#### 4.4.2 存储方式

在`setting.py`中, 可以设置session数据的存储方式, 可以保存在数据库, 本地缓存等.

1. 保存在数据库中

    - Django默认将session保存在数据库(非redis)中, 默认配置如下

    ```python
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'
    ```

    - 如果使用数据库保存session数据, 则必须在`INSTALLED_APPS`中添加上`django.contrib.sessions`(默认是已经添加的)

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions', # 这一项必须配置
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

    > 此时如果进行数据库迁移, 就会看到数据库中有一张`django_session`表
    >
    > 字段为`session_key`, `session_data`, `expire_date`
    >
    > 分别表示session_id, session记录的值, 过期时间

2. 保存本地缓存中

    - 存储在本机内存中, 不能够持久化存储, 也不能在服务器集群中共享, 但是读写速度比较快, 配置为

    ```python
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    ```

3. 混合存储

    - 优先从本机内存中存取，如果没有则从数据库中存取, 配置为
    
    ```python
    SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
    ```

4. 保存在Redis中

    - 如果想要保存在Redis中, 需要安装`django-redis`这个第三方应用

    - 再做如下配置

    ```python
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
    ```

    > 在服务器与redis分离的环境下记得修改对应的配置

#### 4.4.3 Session操作

通过`HttpResponse`对象的`session`属性进行会话的读写操作

1. 写入session

    ```python
    request.session["key"] = "value"
    ```

2. 读取

    ```python
    request.session.get("key", "default")
    ```

3. 清除session中所有**键值对数据**, 保留`session_id`

    ```python
    request.session.clear()
    ```

4. 删除整条session，包括`session_id`和所有数据

    ```python
    request.session.flash()
    ```

5. 删除session中指定的键值对

    ```python
    del request.session["key"]
    ```

6. 设置session的有效期

    ```python
    request.session.set_expiry(value)
    ```
    
    - 如果value是一个`整数`，session将在value秒没有活动后过期

    - 如果value为`0`，那么用户session的Cookie将在用户的浏览器关闭时过
    
    - 如果value为`None`，那么session有效期将采用系统默认值，默认为两周，可以通过在`settings.py`中设置`SESSION_COOKIE_AGE`来设置全局默认值。

    - value还可以是一个`timedelta`对象

<br>
<br>
<br>

## 5. 类视图与中间件

### 5.1 类视图

#### 5.1.1 为什么要使用类视图

- 使用**视图函数**的方式虽然方便, 但是在处理同一个URL请求不同的方法时每次都需要判断`request.method`, 相当麻烦

- 函数的可读性和**复用性**都不强

- 于是在Django中, 可以使用类来定义一个视图, 成为**类视图**

    ```python
    from django.views.generic import View

    class RegisterView(View):
        def get(self, request):
            """处理get请求"""
            return render(request, "register.html")
        
        def post(self, request):
            """处理post请求"""
            return HttpResponse("这里实现注册逻辑")
    ```

- 类视图的好处:

    - 可读性好, 一个实例方法对应一个请求方式

    - 可以继承, 具有复用性

> django.views.generic的模块中, 还有许多有用的**通用视图**类
>
> [Django官方教程 - 通用视图](https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial04/#amend-views)

#### 5.1.2 类视图的使用

- 如上述例子所述, 自定义的类必须继承自`View`类

- 在注册路由时, 使用`.as_view()`方法

    ```python
    urlpatterns = [
        # 类视图的注册
        url(r"^register/$", views.RegisterView.as_view(), name="register")
    ]
    ```

#### 5.1.3 类视图的原理

- 打开Django的源码, 可以看到`View`类中的`as_view()`方法

    ```python
    @classonlymethod
    def as_view(cls, **initkwargs):
        """
        Main entry point for a request-response process.
        """
        ......

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.request = request
            self.args = args
            self.kwargs = kwargs
            # 调用dispatch方法，按照不同请求方式调用不同请求方法
            return self.dispatch(request, *args, **kwargs)

        ......

        # 返回真正的函数视图
        return view


    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
    ```

#### 5.1.4 类视图使用装饰器

1. 为了给类中的实例方法添加装饰器, 需要指定装饰器的第一个参数为`self`, 用于接收该实例的引用

    ```python
    def d(f):
        def wrapper(self, request, *a, **kw):
            print("extra progress")
            return f(self, request, *a, **kw)
        return wrapper
    
    class A(View):
        @d
        def get(self, request):
            print("orignal function")
            return HttpResponse("OK")
    ```

2. 如果我们想加强装饰器的**通用性**, 第一个`self`参数就会造成不小的麻烦, 下面定义一个通用的装饰器和视图类. 有两种方式为类视图添加装饰器

    ```python
    def my_decorator(func):
        def wrapper(request, *args, **kwargs):
            print('自定义装饰器被调用了')
            print('请求路径%s' % request.path)
            return func(request, *args, **kwargs)
        return wrapper
    ```

    - 第一种方式: `urlpatterns`中添加

    ```python
    # 由于DemoView在调用.as_view()是会转转换成函数, 于是可以在urlpatterns中设置
    urlpatterns = [
        url(r"^demo/$", my_decorator(DemoView.as_view*())
    ]
    # 这种方法的坏处是将所有的方法都加上了装饰器的功能, 不能自主选择
    ```
    
    - 第二种方式: `method_decorator`装饰器

    ```python
    from django.utils.decorators import method_decorator
    # 为全部请求方法添加装饰器
    @method_decorator(my_decorator, name='dispatch')
    class DemoView(View):
        def get(self, request):
            print('get方法')
            return HttpResponse('ok')

        def post(self, request):
            print('post方法')
            return HttpResponse('ok')


    # 为特定请求方法添加装饰器1
    @method_decorator(my_decorator, name='get')
    class DemoView(View):
        def get(self, request):
            print('get方法')
            return HttpResponse('ok')

        def post(self, request):
            print('post方法')
            return HttpResponse('ok')

    # 为特定请求方法添加装饰器2
    class DemoView2(View):

        @method_decorator(my_decorator)  # 为get方法添加了装饰器
        def get(self, request):
            print('get方法')
            return HttpResponse('ok')

        @method_decorator(my_decorator)  # 为post方法添加了装饰器
        def post(self, request):
            print('post方法')
            return HttpResponse('ok')

        def put(self, request):  # 没有为put方法添加装饰器
            print('put方法')
            return HttpResponse('ok')
    ```

#### 5.1.5 类视图Mixin拓展

[什么是Mixin](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318680104044a55f4a9dbf8452caf71e8dc68b75a18000)

> `MixIn`的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个`MixIn`的功能，而不是设计多层次的复杂的继承关系。

- Mixin的设计可以让Django中的类视图有更强的拓展性, 提高代码的复用性

    ```python
    class ListModelMixin(object):
        """
        list扩展类
        """
        def list(self, request, *args, **kwargs):
            pass

    class CreateModelMixin(object):
        """
        create扩展类
        """
        def create(self, request, *args, **kwargs):
            pass

    class BooksView(CreateModelMixin, ListModelMixin, View):
        """
        同时继承两个扩展类，复用list和create方法
        """
        def get(self, request):
            self.list(request)
            pass

        def post(self, request):
            self.create(request)
            pass

    class SaveOrderView(CreateModelMixin, View):
        """
        继承CreateModelMixin扩展类，复用create方法
        """
        def post(self, request):
            self.create(request)
            pass
    ```

<br>

### 5.2 中间件

Django中的中间件是一个轻量级, 底层的插件系统, 可以介入Django的请求和响应处理过程, 修改Django的输入或输出. 中间件的设计为开发者提供了一种**无入侵**的开发方式, 增强了Django框架的健壮性

**使用中间件, 在Django处理视图的不同阶段对输入或输出进行干预**

> 使用中间件会处理所有的请求和响应

#### 5.2.1 中间件的定义方法

- 定义一个中间件拥有十分固定的格式

- 需要一个可调用对象, 接受`get_response`这个参数, 该可调用对象必须返回一个可调用对象, 被返回的可调用对象也必须接受一次参数`request`, 并且这个被返回的可调用对象中需要调用`get_response`这个参数(说明这个参数也是一个函数). 乱的一批, 看代码

    ```python
    def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用
        return response
    return middleware
    ```

- 定义好中间件之后也必须在`setting.py`中注册

    ```python
    MIDDLEWARE = [
        # 省略其他默认的中间件
        ....,
        "users.middleware.my_decorator", # 在这里添加
    ]
    ```

#### 5.2.2 执行流程

#### 5.2.3 多个中间件的执行顺序

- 这里的顺序就是`setting.py`中`MIDDLEWARE`常量列表中的排列顺序

- 在请求视图被处理前，中间件**由上至下**依次执行

- 在请求视图被处理后，中间件**由下至上**依次执行

- 在Django初始化时, 中间件**由下至上**一次执行

> 这种调用方式让我觉得`get_response`函数应该是使用了`yeild`来处理了(等待验证)

<br>
<br>
<br>

## 6. 模板

### 6.1 配置

- 在工程中创建模板目录templates

- 在`setting.py`配置文件中修改`TEMPLATES`配置项的`DIRS`的值

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 此处修改
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

### 6.2 渲染模板

1. 调用`loader.get_template(模板文件相对路径)`返回模板对象

2. 调用`模板对象.render(context=None, request=None)`返回渲染后的html文本, 字符串context为模板变量字典, request为请求对象

    ```python
    from django.http import HttpResponse
    from django.template import loader

    def index(request):
        # 1.获取模板
        template=loader.get_template('index.html')

        context={'city': '北京'}
        # 2.渲染模板
        return HttpResponse(template.render(context))
    ```

- Django提供了一个`render()`函数可以简写上述代码

    ```python
    from django.shortcuts import render

    def index(request):
        context={'city': '北京'}
        return render(request,'index.html',context)
    ```

### 6.3 模板语法

> 由于Jinja2参考了Django的模板设计思路, 因此Jinja2中的模板语法都可以使用

1. 模板变量

    - 变量名必须由字母、数字、下划线（不能以下划线开头）和点组成
    
    ```python
    {{变量}}
    ```

    - 模板变量可以使用Python的内建类型, 也可以是对象

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <h1>{{ city }}</h1>
        <h1>{{ adict }}</h1>
        <h1>{{ adict.name }}</h1>  注意字典的取值方法
        <h1>{{ alist }}</h1>  
        <h1>{{ alist.0 }}</h1>  注意列表的取值方法
    </body>
    </html>
    ```

2. 模板语句

    1. for循环
    
    ```html
    {% for item in 列表 %}

    循环逻辑
    {{forloop.counter}}表示当前是第几次循环，从1开始
    {%empty%} 列表为空或不存在时执行此逻辑

    {% endfor %}
    ```
    
    2. if条件

    ```html
    {% if a == 1 %} <!--注意==符号和两边必须留空格-->
    逻辑1
    {% elif ... %}
    逻辑2
    {% else %}
    逻辑3
    {% endif %}
    ```

3. 过滤器

    - 使用管道符号`|`来应用过滤器，用于进行计算、转换操作，可以使用在变量、标签中

    - 如果过滤器需要参数，则使用冒号`:`传递参数
    
    ```
    变量|过滤器:参数
    ```

    - `safe`，禁用转义，告诉模板这个变量是安全的，可以解释执行

    - `length`，长度，返回字符串包含字符的个数，或列表、元组、字典的元素个数

    - `default`，默认值，如果变量不存在时则返回默认值。

    - `date`，日期，用于对日期类型的值进行字符串格式化，常用的格式化字符如下：

        - Y表示年，格式为4位，y表示两位的年

        - m表示月，格式为01,02,12等

        - d表示日, 格式为01,02等

        - j表示日，格式为1,2等

        - H表示时，24进制，h表示12进制的时

        - i表示分，为0-59

        - s表示秒，为0-59

4. 模板继承

    - 父模板

    ```html
    {% block 名称 %}
    预留区域，可以编写默认内容，也可以没有默认内容
    {% endblock  名称 %}
    ```

    - 子模板

    ```html
    {% extends "父模板路径"%}
    
    {% block 名称 %}
    实际填充内容
    {{ block.super }}用于获取父模板中block的内容, 不写直接覆盖父模板内容
    {% endblock 名称 %}
    ```

<br>
<br>
<br>

## 7. 数据库

[Django官方教程-数据库](https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial02/)

在Django中自带了ORM框架, 可以十分方便的操作数据库

使用django进行数据库开发的步骤如下：

1. 配置数据库连接信息

2. 在models.py中定义模型类

3. 迁移

4. 通过类和对象完成数据增删改查操作

### 7.1 数据库配置

在Django中默认使用的数据库为`sqlite`, 如果需要使用`MySQL`需要如下配置

1. 安装MySQL驱动 `pip install pymysql`

2. 在Django工程同名子目录的`__init__.py`文件中添加

    ```python
    from pymysql import install_as_MySQLdb
    
    # 作用是让Django的ORM能以mysqldb的方式来调用PyMySQL
    install_as_MySQLdb()
    ```

3. 修改`setting.py`中**DATABASES**配置信息

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',  # 数据库主机
            'PORT': 3306,  # 数据库端口
            'USER': 'root',  # 数据库用户名
            'PASSWORD': 'mysql',  # 数据库用户密码
            'NAME': 'django_demo'  # 数据库名字
        }
    }
    ```

> 由于使用了`django_demo`这个数据库, 必须在MySQL中创建这个数据库

<br>

### 7.2 定义模型类

- 模型类被定义在`子应用/models.py`下

- 自定义模型类必须继承自`django.db.models.Model`类

#### 7.2.1 定义

- 创建应用booktest, 创建模型

    ```python
    from django.db import models

    #定义图书模型类BookInfo
    class BookInfo(models.Model):
        btitle = models.CharField(max_length=20, verbose_name='名称')
        bpub_date = models.DateField(verbose_name='发布日期')
        bread = models.IntegerField(default=0, verbose_name='阅读量')
        bcomment = models.IntegerField(default=0, verbose_name='评论量')
        is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

        class Meta:
            db_table = 'tb_books'  # 指明数据库表名
            verbose_name = '图书'  # 在admin站点中显示的名称
            verbose_name_plural = verbose_name  # 显示的复数名称

        def __str__(self):
            """定义每个数据对象的显示信息"""
            return self.btitle

    #定义英雄模型类HeroInfo
    class HeroInfo(models.Model):
        GENDER_CHOICES = (
            (0, 'male'),
            (1, 'female')
        )
        hname = models.CharField(max_length=20, verbose_name='名称') 
        hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')  
        hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息') 
        hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
        is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
        
        # 自动生成的两个字段, 可以在模型实例中设置
        # ID = 主键
        # hbook_id = 外键字段名

        class Meta:
            db_table = 'tb_heros'
            verbose_name = '英雄'
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.hname
    ```

1. 数据库表名

    - 模型类如果未指明表名, Django默认以**小写 应用名_小写模型类名** 为数据库表名

    - 也可以通过`db_table`来知名数据库表名

2. 主键

    - Django会为表创建自动增长的主键列吗每个模型只能有一个主键列, 如果使用手动设置了某列为主键, Django就不会创建自动增长的主键列

    - 默认创建的主键列属性为id, 可以用pk代替

3. 属性命名的限制

    - 不能使Python的关键字

    - 不允许使用连续的下划线, 连续的下划线是Django中的查询方式

    - 定义属性时需要指定字段类型, 通过字段类型的参数指定选项
    
    ```python
    属性 = models.字段类型(选项)
    ```

4. 字段类型

    |类型|说明|
    |---|---|
    |AutoField|自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性|
    |BooleanField|布尔字段，值为True或False|
    |NullBooleanField|支持Null、True、False三种值|
    |CharField|字符串，参数max_length表示最大字符个数|
    |TextField|大文本字段，一般超过4000个字符时使用|
    |IntegerField|整数|
    |DecimalField|十进制浮点数， 参数max_digits表示总位数， 参数decimal_places表示小数位数|
    |FloatField|浮点数|
    |DateField|日期， 参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为False； 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为False; 参数auto_now_add和auto_now是相互排斥的，组合将会发生错误|
    |TimeField|时间，参数同DateField|
    |DateTimeField|日期时间，参数同DateField|
    |FileField|上传文件字段|
    |ImageField|继承于FileField，对上传的内容进行校验，确保是有效的图片|

5. 选项

    |选项|说明|
    |---|---|
    |null|如果为True，表示允许为空，默认值是False|
    |blank|如果为True，则该字段允许为空白，默认值是False|
    |db_column|字段的名称，如果未指定，则使用属性的名称|
    |db_index|若值为True, 则在表中会为此字段创建索引，默认值是False|
    |default|默认值|
    |primary_key|若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用|
    |unique|如果为True, 这个字段在表中必须有唯一值，默认值是False|

    - `null`是数据库范畴的概念，`blank`是表单验证范畴的

> 参考: [从模型创建表单](https://docs.djangoproject.com/zh-hans/2.1/topics/forms/modelforms/)

6. 外键
    
    - 在设置外键时, 需要通过`on_delete`选项知名主表删除数据时, 对于外键引用表数据如何处理, 在`django.db.models`中包含了可选常量:

    - `CASCADE` 级联，删除主表数据时连通一起删除外键表中数据

    - `PROTECT` 保护，通过抛出`ProtectedError`异常，来阻止删除主表中被外键应用的数据

    - `SET_NULL` 设置为NULL，仅在该字段null=True允许为null时可用

    - `SET_DEFAULT` 设置为默认值，仅在该字段设置了默认值时可用

    - `SET()` 设置为特定值或者调用特定方法，如

    ```python
    from django.conf import settings
    from django.contrib.auth import get_user_model
    from django.db import models

    def get_sentinel_user():
        return get_user_model().objects.get_or_create(username='deleted')[0]

    class MyModel(models.Model):
        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.SET(get_sentinel_user),
        )
    ```

    - `DO_NOTHING`不做任何操作, 如果数据库前置指明级联性, 此选项会抛出`IntegrityError`异常

#### 7.2.2 定义

将模型类同步到数据库中

1. 生成迁移文件

    ```python
    python manage.py makemigrations
    ```

2. 同步到数据库

    ```python
    python manage.py migrate
    ```

<br>

### 7.3 演示工具的使用

#### 7.3.1 shell工具

Django的manage工具提供了`shell`命令, 帮助我们配置好了当前工程的数据环境(如连接了数据库等), 以便可以直接在工段中执行测试python语句

- 进入shell工具(如果安装了ipython可以通过ipython进行操作)
    
    ```sh
    python manage.py shell
    ```
    
<br>

### 7.4 数据库的增删改查

#### 7.4.1 增

1. `模型对象.save()`方法

2. `模型类.objects.create()`方法

#### 7.4.2 查

- `模型类.objects`是一个`django.db.models.manager.Manager`类的对象

1. 基本查询

    - `模型类.objects.get(查询条件)`查询条件可以是主键(pk), 也可以某个字段

    - `模型类.objects.all()`查询该表中所有数据, 返回`QuerySet`对象(类似于列表, 后面会详细说明)

    - `模型类.objects.count()`返回查询结果数量, `int`类型

    > 对于查询不存在的数据, 会抛出`DoesNotExist`的异常

2. 过滤查询

    - `filter`过滤出多个结果

    - `exclude`排除掉符合条件剩下的结果

    - `get`过滤单一结果

    ```python
    # 过滤条件语法如下
    属性名称__查询方式=值
    # 属性名和比较运算符间使用两个下划线, 所以属性名不能包括多个下划线
    ```

    - 返回的是`QuerySet`对象, 如果查询不到返回空的`QuerySet`对象
    
    1. 相等 `exact`

    ```python
    BookInfo.objects.filter(id__exact=1)
    # 简写
    BookInfo.objects.filter(id=1)
    ```

    2. 模糊查询 `endswith, startswith, contains`
    
    ```python
    # 如果包含%无需转译, 可以直接写
    BookInfo.objects.filter(btitle__contains='传')  # 包含
    BookInfo.objects.filter(btitle__endswith='传')  # 以结尾
    BookInfo.objects.filter(btitle__startswith='传')  # 以开头
    ```

    > 上面的查询都是大小写敏感的, 如果希望查询大小写不敏感的可以在前面加i, 如 iexact, iendswith, istartswith, icontains

    3. 空查询 `isnull`

    ```python
    # 查询书名不为空的书
    BookInfo.objects.filter(btitle__isnull=False)
    ```

    4. 范围查询 `in`

    ```python
    # 查询编号为1, 3的书
    BookInfo.objects.filter(id__in=[1, 3])
    ```
    
    5. 比较查询 `gt(greater then)`, `gte(great then equal)`, `lt`, `lte`

    ```python
    # id大于3的书本
    BookInfo.objects.filter(id__gt=3)
    ```

    6. 日期查询

    ```python
    # year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算
    # 查询1980年的书
    BookInfo.objects.filter(bpub_date__year=1980)
    # 查询1980年后发表的书
    BookInfo.objects.filter(bpub_date__gt=date(1980,1,1))
    ```

    7. **F对象**, 比较两个属性(而不是将某属性和固定值比较)

    ```python
    from django.db.models import F

    # 查询阅读数大于评论数的书籍
    BookInfo.objects.filter(bread__gte=F('bcomment'))
    # 查询阅读量大于评论量2呗的书籍
    BookInfo.objects.filter(bread__gt=F('bcomment')*2)
    ```

    8. **Q**对象, 能够连接查询条件, `&==and`, `|==or`, `~==not`

    ```python
    # 查询阅读量大于20 且and 编号小于3的图书
    BookInfo.objects.filter(bread__gt=20, id__lt=3)
    # 或者
    BookInfo.objects.filter(bread__gt=20).filter(id__lt=3)

    # Q(属性名__条件=值)
    # 查询阅读量大于20 且 编号小于3的书, 改写为Q对象
    from django.db.models import Q

    BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))

    # 查询阅读量大于20 或 编号小于3的书
    BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
    
    # 查询编号不等于3的图书
    BookInfo.objects.filter(~Q(pk=3))
    ```

    9. 聚合函数, `aggregate()`可以调用聚合函数, 聚合函数需要额外导入

    ```python
    # 
    from django.db.models import Sum
    
    # 查询图书的总阅读量
    BookInfo.objects.aggregate(Sum('bread'))
    ```

    > 注意: 使用聚合函数查询返回字典类型, 格式如下: {"属性__聚合函数名":值}

3. 排序

    1. 使用`order_by`对结果进行排序

    ```python
    BookInfo.objects.all().order_by('bread')  # 升序
    BookInfo.objects.all().order_by('-bread')  # 降序
    ```

4. 关联查询
    
    - 在一对多的关系中, 快速查找对应模型对象(类似于SQLAlchemy中的关系属性)

    1. 通过一找到多, 在一的模型中自动生成了`.多的模型类_set`这样一个属性, 类型为`RelatedManager`, 和`Manager`对象方法一样

    ```python
    # 查询第一本书出现的所有英雄人物
    book = BookInfo.objects.get(id=1)
    book.heroinfo_set.all()
    ```

    2. 通过多找到一, 直接读取设置外键的那个属性, 返回一个一的模型对象

    ```python
    hero = HeroInfo.objects.get(pk=1)
    # 取到对应的模型对象
    book = hero.hbook
    # 有的时候不需要取到整个对象, 直接取对应对象的id
    book_id = hero.hbook_id  # 这个属性不用设置, 会自动生成
    ```

5. 关联过滤查询

    - 有些像连接查询或者子查询

    1. 通过多找到一, 添加过滤条件

    ```python
    # 注意这里的heroinfo是自动生成的, 上面的那个heroinfo_set也是自动产生的
    # 查询图书, 要求该书中有英雄人物名字叫做孙悟空
    BookInfo.objects.filter(heroinfo__hname="孙悟空")
    # 查询图书, 要求该书中有英雄人物名字包含空
    BookInfo.objects.filter(heroinfo__hname__contains="八")
    ```

    2. 通过一找到多, 添加查询条件

    ```python
    # 同一个套路
    # 查询天龙八部所有的英雄
    HeroInfo.objects.filter(hbook__btitle="天龙八部")
    # 等于
    BookInfo.objects.get(btitle="天龙八部").heroinfo_set.all()

    # 查询阅读量大于30的图书的所有英雄人物
    HeroInfo.objects.filter(hbook__bread__gt=30)
    # 这个如果想用书去查的话就有点难受了
    ```

#### 7.4.3 改

有两种修改的方法

1. save()
    
    ```python
    hero_char = HeroInfo.objects.get(hname="孙悟空")
    hero.hame = "孙行者"
    hero.save()
    ```

2. update() 

    ```python
    # 使用模型类.objects.filter().update()，会返回受影响的行数
    HeroInfo.objects.filter(hname="孙行者").update(hname="孙悟空")
    ```

#### 7.4.4 删除

1. 模型对象的`.delete()`方法

2. 模型类的`.objects.filter().deleted()`方法

<br>

### 7.5 查询集QuerySet

#### 7.5.1 概念

如果从数据库中查询了**多个**模型的实例, Django将会将这些查询对象统一放到`QuerySet`这个容器中

下面几种方法查询出来的结果都是获得`QuerySet`对象

- `all()`:返回所有数据

- `filter()`:返回满足条件的数据

- `exclude()`:返回满足条件之外的数据

- `order_by()`:对结果进行排序

如果没有查询到, Django也会返回一个`QuerySet`对象

- `exists()`: 查看`QuerySet`是否为空

#### 7.5.2 几个好处

1. 惰性查询

    - 使用查询条件进行查询返回`QuerySet`对象时, 本质上是将**对应的SQL语句保存在对象内部**, 当进一步取值的时候才会Python才会与数据库交互

    ```python
    # 获取QuerySet对象, 此时没有查询
    # 此时在qs内部保存了sql语句, select * from BookInfo
    qs = BookInfo.objects.all()

    # 取值, 此时会执行sql语句
    for book in qs:
        print(book)
    ```

2. 缓存机制

    - 一旦`QuerySet`对象进行了查询, 他会在对象内部保存**已经查询好的数据**, 这样再次取值的时候实际上是从**对象内部的属性**中取值的

    ```python
    # 获取QuerySet对象, 此时没有查询
    # 此时在qs内部保存了sql语句, select * from BookInfo
    qs = BookInfo.objects.all()

    # 取值, 此时会执行sql语句
    ls1 = [book.btitle for book in qs]

    # 不会再去与数据库交互
    ls2 = [book.btitle for book in qs]
    ```

3. 链式调用

    - `QuerySet`对象后面还可以去接其他的过滤条件, 获取的是另外的`QuerySet`对象

    ```python
    # 获取QuerySet对象, 此时没有查询
    # 此时在qs内部保存了sql语句, select * from BookInfo
    qs = BookInfo.objects.all()
    
    # 新的QS对象被构建
    # 此时qs2内部的sql语句为 select * from BookInfo where btitle like "%传%"
    qs2 = qs.filter(btitile__contains="传")
    ```

#### 7.5.3 限制查询集

`QuerySet`还支持切片和索引

- 使用切片相当于在mysql中使用了`limit`关键字, 返回的同样也是一个`QuerySet`对象

    ```python
    qs = BookInfo.objects.all()[0:2]
    ```

- 使用索引则是只查询一个值, 返回一个对象, 如果不存在则抛出`DoesNotExist`异常

<br>

### 7.6 管理器Manager

管理器是Django的模型与数据库交互的接口, Django应用的美国模型类都拥有至少一个管理器

`模型类.objects`获得的就是一个`Manager`对象

#### 7.6.1 自定义管理器

模型类可以使用自定义的管理器.

但是一旦应用了自定义管理器就不能使用Django默认的管理器, 换句话说就不能使用`模型类.objects`来获得管理器对象了

自定义管理器主要用于以下两个场景

1. 修改原始查询集, 重写all()方法

    ```python
    #图书管理器
    class BookInfoManager(models.Manager):
        def all(self):
            #默认查询未删除的图书信息
            #调用父类的成员语法为：super().方法名
            return super().filter(is_delete=False)
    
    # 在模型中定义管理器实例
    class BookInfo(models.Model):
        ...
        books = BookInfoManager()

    # 使用
    BookInfo.books.all()
    ```

2. 在管理器类中补充新的方法

    ```python
    class BookInfoManager(models.Manager):
        #创建模型类，接收参数为属性赋值
        def create_book(self, title, pub_date):
            #创建模型类对象self.model可以获得模型类
            book = self.model()
            book.btitle = title
            book.bpub_date = pub_date
            book.bread=0
            book.bcommet=0
            book.is_delete = False
            # 将数据插入进数据表
            book.save()
            return book

    # 在模型中定义管理器实例
    class BookInfo(models.Model):
        ...
        books = BookInfoManager()
    
    # 调用方法
    book=BookInfo.books.create_book("abc",date(1984,1,1))
    ```
    
<br>
<br>
<br>

## 8. Admin站点

在Django中, 可以通过简单的配置使用自带的后台系统去管理数据库

### 8.1 简单的配置

1. 配置本地化界面

    - 在主应用的setting.py中设置地区

    ```python
    # setting.py
    LANGUAGE_CODE = 'zh-hans' # 使用中国语言
    TIME_ZONE = 'Asia/Shanghai' # 使用中国上海时间
    ```

2. 创建超级管理员

    - 创建好了就可以从`/admin`登录去了

    ```python
    python manage.py createsuperuser
    ```

3. 配置子应用

    - 如果想让后台页面显示可读的名字, 需要设置`apps.py`

    ```python
    from django.apps import AppConfig

    class BooktestConfig(AppConfig):
        name = 'booktest'
        # 在模型中, 字段也能设置verbose_name , 这就是专门显示在后台中的
        verbose_name = '图书管理'  
    ```

4. 注册模型类

    - 进入自应用的`admin.py`文件中设置需要后台显示的数据模型

    ```python
    from django.contrib import admin
    from booktest.models import BookInfo,HeroInfo

    admin.site.register(BookInfo)
    admin.site.register(HeroInfo)
    ```

### 8.2 自定义模型显示

- 此时再后台中显示的模型数据显示的信息内容比较少, 为了自定义显示内容, 我们可以自定义一个Admin管理类

    ```python
    from django.contrib import admin
    from booktest.models import BookInfo

    class BookInfoAdmin(admin.ModelAdmin):
        pass
    
    # 注册模型的时候第二个参数传入自定义Admin
    admin.site.register(BookInfo,BookInfoAdmin)
    ```

1. 调整列表页的显示

    ```python
    class BookInfoAdmin(admin.ModelAdmin):
        list_per_page=100  # 每页数据条数
        actions_on_top=True # 顶部显示的操作选项
        actions_on_bottom=False  # 底部显示的操作选项
        list_display = ['id','btitle']  # 显示那些字段的信息

        # 通过设置short_description属性，可以设置在admin站点中显示的列名
        def pub_date(self):
            return self.bpub_date.strftime('%Y年%m月%d日')

        pub_date.short_description = '发布日期'  # 设置方法字段在admin中显示的标题
        pub_date.admin_order_field = 'bpub_date'  # 自定义的字段不能够排序, 设置该属性可以指定按某字段排序

    
    class HeroInfo(models.Model):
        
        # 设置关联对象, 
        def read(self):
            return self.hbook.bread

        read.short_description = '图书阅读量'

        # 当设置了管理对象后, 可以显示该对象
        list_display = ['id', 'hname', 'hbook', 'read']

        list_filter = ['hbook', 'hgender'] # 设置右侧的过滤栏

        search_fields = ['hname']  # 搜索框, 以某字段来搜索内容
    ```

2. 调整编辑页的显示

    - 但点击一条记录可以对某一条记录进行编辑

    ```python
    class BookInfoAdmin(admin.ModelAdmin):
        ...
        fields = ['btitle', 'bpub_date']  # 只能编辑这两个字段的内容
        
        # 设置分组显示 和上面二者选一
        fieldsets = (
            ('基本', {'fields': ['btitle', 'bpub_date']}),
            ('高级', {
                'fields': ['bread', 'bcomment'],
                'classes': ('collapse',)  # 是否折叠显示
            })
        )

        # 格式如下
        # fieldset=(
        #    ('组1标题',{'fields':('字段1','字段2')}),
        #    ('组2标题',{'fields':('字段3','字段4')}),
        #)
    ```
    
    - 在一对多的关系中, 可以在'一'端的编辑页面中编辑'多'端的对象, 也只需要一些简单的配置
    
    ```python
    # 以块状的方式显示编辑信息
    class HeroInfoStackInline(admin.StackedInline):
        model = HeroInfo  # 要编辑的对象
        extra = 1  # 附加编辑的数量
    
    # 以表格的形式
    class HeroInfoTabularInline(admin.TabularInline):
        model = HeroInfo
        extra = 1 
    
    class BookInfoAdmin(admin.ModelAdmin):
        ...
        # 在一的一方设置inlines属性, 添加自己想要的显示方式
        inlines = [HeroInfoStackInline]
        # inlines = [HeroInfoTabularInline]
    ```

3. 调整站点信息

    - 编辑子应用下面的`admin.py`文件

    ```python
    from django.contrib import admin

    admin.site.site_header = 'BookManagementSystem'
    admin.site.site_title = 'DMS'
    admin.site.index_title = 'Welcome to DMS!'
    ```

4. 上传图片

    - 需要安装`pillow`

    - 默认情况下Django会将上传的图片保存在本地, 因此需要配置上传的目录

    ```python
    # setting.py
    MEDIA_ROOT=os.path.join(BASE_DIR,"static_files/media")
    # static_files是之前通过 STATICFILES_DIRS 设置的
    ```

    - 想为某个模型添加图片信息, 需要在模型中添加字段

    ```python
    class BookInfo(models.Model):
        ...
        # upload_to 选项指明该字段的图片保存在MEDIA_ROOT目录中的哪个子目录
        image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)
    ```

    - 别忘了数据库迁移命令!

    - 此时再后台中可以为数据上传图片了, 而image字段只保存图片的路径, 因此类型是varchar.
