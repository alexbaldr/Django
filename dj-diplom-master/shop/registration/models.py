from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    username = models.OneToOneField(User, verbose_name="Клиент",
                                    on_delete=models.DO_NOTHING,
                                    null=False, blank=False)

    def __str__(self):
        return self.username
