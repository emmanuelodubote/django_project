

import os
import django
from MainApp.models import Topic, Entry


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

django.setup()

print()
topics = Topic.objects.all()

for t in topics:
    print(f'ID: {t.id}, Name: {t.text}')

print()




t = Topic.objects.get(id = 1)

# t = Topic.objects.get(text = 'Rock Climbing')

print(t.text)
print(t.date_added)
print()



# entries = Entry.objects.get(topic = 1)

entries = t.entry_set.all()

for entry in entries:
    print(entry)
    # print(entry.text)

print()

