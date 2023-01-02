from django.db import models
from django.contrib.auth.models import User
import datetime

class Application(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    link = models.URLField(max_length=250, blank=False, unique=True)
    application_date = models.DateField(default=datetime.date.today(),blank=False)
    response_date = models.DateField(null=True, blank=True)
    rejection_date = models.DateField(null = True, blank=True)
    cv_included = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def was_added_recently(self):
        return self.application_date >= timezone.now() - datetime.timedelta(days=7)