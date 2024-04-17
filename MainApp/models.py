from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #here topic isn't just an attr (topic id) but an obj that contains the id (bcos of the FK)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        #it allows us to set a special attribute tellign Django to use 'Entries'
        # when it needs to refer to more than one entry. Without this, Django
        # would refer to multiple as 'Entrys'.
        verbose_name_plural = 'entries'

    def __str__(self):  
        return f"{self.text[:50]}..."


