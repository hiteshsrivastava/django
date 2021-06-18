from django.db import models

class users (models.Model):
    uname = models.CharField(max_lenght = 100)
    uemail = models.EmailField(max_lenght = 100)
    upassword = models.CharField(max_lenght = 100)
    ucontact = models.CharField(max_lenght = 30)

