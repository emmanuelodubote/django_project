from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')


def topics(request):

    # object name
    topics = Topic.objects.all().order_by('date_added')
    
    # key (template variable): variable name that would be used in the template
    # value (obj/view/function var): variable name (obj) used in the view to retrieve data from the DB
    context = {'t_topics': topics}

    return render(request, 'MainApp/topics.html', context)


# the name given to the topic_id here must be consistent with the url link in urls
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    #after the user clicks the topic the want to view, the app filters based on the topic the selected (using the topic id), and then produce/display all entries that is related to the topic (topic id) selected
    entries = Entry.objects.filter(topic=topic).order_by('-date_added') #here the orange topic is an obj (from the models file), so obj must be compared with obj hence why the white isn't topic_id but called from the main Obj itself Topic. Remember that both are referring to the topic id regardless of them being an obj
    
    context = {'topic': topic, 'entries': entries}

    return render(request, 'MainApp/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return redirect('MainApp:topic', topic_id=topic_id)

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)



