from django.db import models

# Create your models here.


class Mails(models.Model):
    id = models.BigAutoField(primary_key=True)
    mail_text = models.TextField()
    classifier = models.IntegerField()

    class Meta:
        app_label = "storage"
