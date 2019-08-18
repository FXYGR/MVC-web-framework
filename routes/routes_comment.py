from models.comment import Comment
from routes import login_required, current_user, redirect, html_response
from utils import log


def add(request):
    u = current_user(request)
    form = request.form()
    log('comment_add form:', form)
    # weibo_id = int(form['weibo_id'])

    form['user_id'] = u.id
    # form['weibo_id'] = weibo_id
    Comment.new(form)

    log('comment add', u, form)
    return redirect('/weibo/index')


def delete(request):
    comment_id = int(request.query['id'])
    Comment.delete(id=comment_id)
    # 注意删除所有微博对应评论
    # cs = Comment.all(weibo_id=weibo_id)
    # for c in cs:
    #     c.delete(c.id)
    return redirect('/weibo/index')


def edit(request):
    comment_id = int(request.query['id'])
    c = Comment.one(id=comment_id)
    return html_response('comment_edit.html', comment=c)


def update(request):
    """
    用于增加新 weibo 的路由函数
    """
    form = request.form()
    comment_id = int(form['id'])
    content = form['content']

    Comment.update(comment_id, content=content)
    # 浏览器发送数据过来被处理后, 重定向到首页
    # 浏览器在请求新首页的时候, 就能看到新增的数据了
    return redirect('/weibo/index')


def comment_owner_required(route_function):
    """
    这个函数看起来非常绕，所以你不懂也没关系
    就直接拿来复制粘贴就好了
    """

    def f(request):
        log('comment_owner_required')
        u = current_user(request)
        if 'id' in request.query:
            comment_id = request.query['id']
        else:
            comment_id = request.form()['id']
        c = Comment.one(id=int(comment_id))

        if c.user_id == u.id:
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
        '/comment/add': login_required(add),
        '/comment/edit': login_required(comment_owner_required(edit)),
        '/comment/update': login_required(comment_owner_required(update)),
        '/comment/delete': login_required(comment_owner_required(delete)),
    }
    return d
