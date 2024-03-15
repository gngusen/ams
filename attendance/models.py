from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default = timezone.now)
    service_name = models.CharField(max_length=200)
    adult_males = models.BigIntegerField(null=True)
    adult_females = models.BigIntegerField(null=True)
    child_males = models.BigIntegerField(null=True)
    child_females = models.BigIntegerField(null=True)
    
    def submit(self):
        self.created_date = timezone.now
        self.save()
        
    def __str__(self):
        return self.service_name