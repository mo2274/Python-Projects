from django.shortcuts import render
from .models import Topic, Entry


# Create your views here.
def index(request):
    """ the home page for learning log """
    return render(request, r'learning_logs\index.html')


def topics(request):
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, r'learning_logs\topics.html', context)


def topic(request, id):
    try:
        entries = Entry.objects.filter(topic_id=id).order_by('date_add')
        topic = Topic.objects.get(id=id)
        context = {'entries': entries, 'topic': topic}
    except Exception:
        return render(request, r'learning_logs\index.html')
    return render(request, r'learning_logs\topic.html', context)
