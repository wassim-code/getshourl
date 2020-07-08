from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=30, unique=True, primary_key=True)
    redirect_url = models.CharField(max_length=200)
    add_tm = models.DateTimeField(auto_now_add=True)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.url