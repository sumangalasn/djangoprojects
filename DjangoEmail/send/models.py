from django.db import models
# Create your models here.
class send(models.Model):
  sent_mail = models.CharField(max_length=200,
    primary_key=True)

  subject = models.TextField(max_length=100)

  text = models.CharField(max_length=40)

  from_mail = models.CharField(max_length=300)

  recipient_mail=models.CharField(max_length=200)

  class Meta:
    db_table = 'send'

