from django.shortcuts import render


# 第一行的 index 是函数名，request 是参数，必须要，因为函数在被调用时，请求会被传入，request 就是对应的参数。
# 第二行 return，这个是返回，函数必须有返回
# render 是 django 内置的渲染函数，这里放入了两个值第一个是 request，默认的，需要加；第二个值是 index.html ，这个是放在 templates 目录中的首页
# render() 函数的结果是一个 Response 响应，每个视图函数都必须返回一个响应。
# Create your views here.
def index(request):
    return render(request, 'index.html')
