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
    context = {'t_topics': topics}          #sending to the template

    return render(request, 'MainApp/topics.html', context)      #sending to the template


# the name given to the topic_id here must be consistent with the url link in urls
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    #after the user clicks the topic they want to view, the app filters based on the topic the selected (using the topic id), and then produce/display all entries that is related to the topic (topic id) selected
    entries = Entry.objects.filter(topic=topic).order_by('-date_added') #here the orange topic is an obj (from the models file), so obj must be compared with obj hence why the white isn't topic_id but called from the main Obj itself Topic. Remember that both are referring to the topic id regardless of them being an obj
    
    context = {'topic': topic, 'entries': entries}

    return render(request, 'MainApp/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():         #for fields validation
            form.save()

            return redirect('MainApp:topics')

    context = {'form':form}         #{key points to the view while the value points to the template. ending the form to the template (line 12 in new_topic.html)
    return render(request, 'MainApp/new_topic.html', context)       #sending the form to the template


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            # form.save()       #using this will cause issue later on hence the alt below. Remember Entry class in the models.py requires a FK. This hasn't been taken care of, hence the below codes.
            new_entry = form.save(commit=False)     #created an obj but not saving to the DB yet
            new_entry.topic = topic                 #added the FK field. Now all required fields stated in the models.py have been taken care of before saving into the DB.
            new_entry.save()

            return redirect('MainApp:topic', topic_id=topic_id)     #topic_id is a variable but topic.id is an attr/column value in an obj. Both will work here bcos in line 50 we made topic an obj variable (emphasis on Obj) using the Topic.Obj func/mtd

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)





def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():                
            form.save()

            return redirect('MainApp:topic', topic_id=topic.id)     

    context = {'form':form, 'topic':topic, 'entry':entry}   #The key is used in the template file, while the value in the view
    return render(request, 'MainApp/edit_entry.html', context)




