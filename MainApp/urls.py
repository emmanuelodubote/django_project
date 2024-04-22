

from django.urls import path, include
from . import views

app_name = 'MainApp'

urlpatterns = [
    
    # 1st Arg (url link), 2nd (points to the view func), 3rd (ignore)
    path('', views.index, name = 'index'),
    path('topics', views.topics, name = 'topics'),
    path('topics/<int:topic_id>', views.topic, name = 'topic'),  # the name given to the topic_id here must be consistent with the func parameters in views
    path('new_topic/', views.new_topic, name = 'new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
]





