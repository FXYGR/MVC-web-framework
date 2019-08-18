from models.comment import Comment
from models.user import User
from models.weibo import Weibo
from routes import (
    redirect,
    current_user,
    html_response,
    login_required,
)
from utils import log


def index(request):
    """
    weibo 首页的路由函数
    """
    u = current_user(request)
    weibos = Weibo.all(user_id=u.id)
    # 替换模板文件中的标记字符串
    return html_response('weibo_index.html', weibos=weibos, user=u)


def add(request):
    """
    用于增加新 weibo 的路由函数
    """
    u = current_user(request)
    form = request.form()
    Weibo.add(form, u.id)
    # 浏览器发送数据过来被处理后, 重定向到首页
    # 浏览器在请求新首页的时候, 就能看到新增的数据了
    return redirect('/weibo/index')


def delete(request):
    weibo_id = int(request.query['id'])
    Weibo.delete(weibo_id)
    # 注意删除所有微博对应评论
    cs = Comment.all(weibo_id=weibo_id)
    for c in cs:
        c.delete(c.id)
    return redirect('/weibo/index')


def edit(request):
    weibo_id = int(request.query['id'])
    w = Weibo.one(id=weibo_id)
    return html_response('weibo_edit.html', weibo=w)


def update(request):
    """
    用于增加新 weibo 的路由函数
    """
    form = request.form()
    weibo_id = int(form['id'])
    content = form['content']
    Weibo.update(weibo_id, content=content)
    # 浏览器发送数据过来被处理后, 重定向到首页
    # 浏览器在请求新首页的时候, 就能看到新增的数据了
    return redirect('/weibo/index')


# def comment_add(request):
#     u = current_user(request)
#     form = request.form()
#     log('comment_add form:', form)
#     # weibo_id = int(form['weibo_id'])
#
#     form['user_id'] = u.id
#     # form['weibo_id'] = weibo_id
#     Comment.new(form)
#
#     log('comment add', u, form)
#     return redirect('/weibo/index')
#
#
# def comment_edit(request):
#     comment_id = int(request.query['id'])
#     c = Comment.one(id=comment_id)
#     return html_response('comment_edit.html', comment=c)
#
#
# def comment_update(request):
#     """
#     用于增加新 weibo 的路由函数
#     """
#     form = request.form()
#     comment_id = int(form['id'])
#     content = form['content']
#
#     Comment.update(comment_id, content=content)
#     # 浏览器发送数据过来被处理后, 重定向到首页
#     # 浏览器在请求新首页的时候, 就能看到新增的数据了
#     return redirect('/weibo/index')


def weibo_owner_required(route_function):
    """
    这个函数看起来非常绕，所以你不懂也没关系
    就直接拿来复制粘贴就好了
    """

    def f(request):
        log('weibo_owner_required')
        u = current_user(request)
        if 'id' in request.query:
            weibo_id = request.query['id']
            log('weibo_owner1', weibo_id)
        else:
            weibo_id = request.form()['id']
            log('weibo_owner2', weibo_id)

        w = Weibo.one(id=int(weibo_id))
        log('weibo_owner_required ', w)

        if w.user_id == u.id:
            return route_function(request)
        else:
            return redirect('/weibo/index')

    return f


def route_dict():
    """
    路由字典
    key 是路由(路由就是 path)
    value 是路由处理函数(就是响应)
    """
    d = {
        '/weibo/add': login_required(add),
        '/weibo/delete': login_required(weibo_owner_required(delete)),
        '/weibo/edit': login_required(weibo_owner_required(edit)),
        '/weibo/update': login_required(weibo_owner_required(update)),
        '/weibo/index': login_required(index),
        # 评论功能
        # '/comment/add': login_required(comment_add),
        # '/comment/edit': login_required(weibo_owner_required(comment_edit)),
        # '/comment/update': login_required(weibo_owner_required(comment_update)),
    }
    return d
