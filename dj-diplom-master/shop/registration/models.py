from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    username = models.OneToOneField (User, verbose_name="Клиент", 
    on_delete=models.DO_NOTHING, null=False, blank=False)
    # date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
