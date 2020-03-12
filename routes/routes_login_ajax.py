from routes import (
    html_response,
    json_response,
)


def index(request):
    """
    todo 首页的路由函数
    """
    # 替换模板文件中的标记字符串
    return html_response('login_ajax.html')


def check_username(request):
    form = request.json()
    username = form['username']
    length = len(username)
    if 2 <= length <= 10 and check_first_and_last(username) and check_in_string(username):
        message = '检查合格'
    else:
        message = '用户名错误'
    data = dict(message=message)
    return json_response(data)


def check_in_string(username):
    right_string = '0123456789_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for s in username:
        if s not in right_string:
            return False
    return True


def check_first_and_last(username):
    begin_end = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if username[0] in begin_end and username[-1] in begin_end:
        return True
    else:
        return False


def route_dict():
    """
    路由字典
    key 是路由(路由就是 path)
    value 是路由处理函数(就是响应)
    """
    d = {
        '/login/ajax/check_username': check_username,
        '/login/ajax/index': index,
    }
    return d
