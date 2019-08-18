from models import Model
from models.base_model import SQLModel
from models.comment import Comment


class Weibo(SQLModel):
    """
    微博类
    """
    sql_create = '''
            CREATE TABLE `weibo` (
                `id`        INT NOT NULL AUTO_INCREMENT,
                `content`   VARCHAR(255) NOT NULL,
                `user_id`   INT NOT NULL,
                PRIMARY KEY (`id`)
            );
         '''

    def __init__(self, form):
        super().__init__(form)
        self.content = form.get('content', '')
        # 和别的数据关联的方式, 用 user_id 表明拥有它的 user 实例
        self.user_id = form.get('user_id', None)

    @classmethod
    def add(cls, form, user_id):
        form['user_id'] = user_id
        cls.new(form)

    # @classmethod
    # def update(cls, form):
    #     weibo_id = int(form['id'])
    #     w = Weibo.find_by(id=weibo_id)
    #     w.title = form['content']
    #     w.save()

    def comments(self):
        cs = Comment.all(weibo_id=self.id)
        return cs