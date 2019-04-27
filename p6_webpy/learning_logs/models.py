from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
添加一个新模型，因此需要再次迁移数据库：
    修改models.py
    执行命令python manage.py makemigrations app_name
    执行命令python manage.py migrate
"""


class Topic(models.Model):
    """用户学习的主题"""

    # 两个属性
    text = models.CharField(max_length=200) # 由字符或文本组成的数据，定义CharField 属性时，必须告诉Django该在数据库中预留多少空间
    date_added = models.DateTimeField(auto_now_add=True) # 记录日期和时间的数据，参数表示自动设置成当前日期和时间
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""

    # topic = models.ForeignKey(Topic)  # django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # topic 是一个ForeignKey 实例
    text = models.TextField()  # 无长度限制
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."
