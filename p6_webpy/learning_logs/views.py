from django.shortcuts import render
from .models import Topic

# views.py是执行命令python manage.py startapp 时自动生成的
# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  # date_added 前面的减号指定按降序排列
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
