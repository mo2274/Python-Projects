from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


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


def new_topic(request):
    """ add new topic """
    if request.method != 'POST':
        """ Create blank form """
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, r'learning_logs\new_topic.html', context)


def new_entry(request, id):
    """ add new entry """
    topic = Topic.objects.get(id=id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic_id = topic
            new_entry.save()
            return redirect('learning_logs:topic', id=id)
    context = {'form': form, 'topic': topic}
    return render(request, r'learning_logs\new_entry.html', context)


def edit_entry(request, id):
    entry = Entry.objects.get(id=id)
    topic = entry.topic_id
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', id=topic.id)
    context = {'entry': entry, 'form': form, 'topic': topic}
    return render(request, r'learning_logs\edit_entry.html', context)
