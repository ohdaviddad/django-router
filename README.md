# django-router

### 起源

看到`beego`的注解路由，想做一个简单的、类似的功能，于是选择给`django`做一个。

### 规则

解析以`#@router`开始的行，将`url`与下一行函数绑定。

### 错误示例

```python
#@router /hello

def hello(request):
    return HttpResponse('Hello Django')
```

- 路由与函数中间间隔一行。

```python
# @router /hello
def hello(request):
    return HttpResponse('Hello Django')
```

- `#`与`@router`中间有空格。

### 创建django项目

```
django-admin startproject test_router
cd test_router
django-admin startapp hello
python manage.py startapp second
```

先创建项目`test_router`，然后使用两种方式，创建应用`hello`和`second`。

### 设置django

```python
# test_router/test_router/settings.py
DEBUG = False
ALLOWED_HOSTS = ['*']
```

复制`router.py`到项目目录。

配置`url`：

```python
# test_router/test_router/urls.py
import router

urlpatterns = []

router.route_map(urlpatterns)
```

### 业务代码

`hello`应用：

```python
from django.shortcuts import HttpResponse

#@router /hello
def hello(request):
    return HttpResponse('Hello Django')

#@router /hello2
def hello2(request):
    return HttpResponse('Hello django-router')
```

`second`应用：

```python
from django.shortcuts import HttpResponse
import time

#@router /second
def second(req):
    t = time.ctime()
    return HttpResponse(f'<h1>{t}</h1>')
```

### 运行

```
python manage.py runserver
```

