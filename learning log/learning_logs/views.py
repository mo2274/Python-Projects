from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

template_name = r"learning_logs/index.html"


def index(request):
    """ the home page for learning log """
    return render(request, r'learning_logs/index.html')


@login_required
def topics(request):
    topics = Topic.objects.filter(user=request.user).order_by('date_add')
    context = {'topics': topics}
    return render(request, r'learning_logs/topics.html', context)


@login_required
def topic(request, id):
    try:
        entries = Entry.objects.filter(topic_id=id).order_by('date_add')
        topic = Topic.objects.get(id=id)
        check_topic_owner(topic, request)
        context = {'entries': entries, 'topic': topic}
    except Exception:
        raise Http404
    return render(request, r'learning_logs/topic.html', context)


def check_topic_owner(topic, request):
    if topic.user != request.user:
        raise Http404


@login_required
def new_topic(request):
    """ add new topic """
    if request.method != 'POST':
        """ Create blank form """
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.user = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, r'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, id):
    """ add new entry """
    topic = Topic.objects.get(id=id)
    check_topic_owner(topic, request)
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
    return render(request, r'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, id):
    entry = Entry.objects.get(id=id)
    topic = entry.topic_id
    check_topic_owner(topic, request)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', id=topic.id)
    context = {'entry': entry, 'form': form, 'topic': topic}
    return render(request, r'learning_logs/edit_entry.html', context)


@login_required
def delete_entry(request, id):
    entry = Entry.objects.get(id=id)
    if not entry:
        raise Http404
    topic = entry.topic_id
    check_topic_owner(topic, request)
    entry.delete()
    return redirect('learning_logs:topic', id=topic.id)


@login_required
def delete_topic(request, id):
    topic = Topic.objects.get(id=id)
    if not topic:
        raise Http404
    check_topic_owner(topic, request)
    topic.delete()
    return redirect('learning_logs:topics')
