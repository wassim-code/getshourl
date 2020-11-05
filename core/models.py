from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=10, unique=True, primary_key=True)
    redirect_url = models.CharField(max_length=200)
    add_tm = models.DateTimeField(auto_now_add=True, verbose_name='add time')
    total_clicks = models.IntegerField(default=0)
    password = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        return self.url
    
    def has_password(self):
        return bool(self.password)

    has_password.boolean = True