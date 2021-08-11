from django.db import models

# Create your models here.


class Events(models.Model):
    event_name = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    time = models.DateTimeField(blank=True)
    location = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name


