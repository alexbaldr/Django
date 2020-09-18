from django.db import models

# Create your models here.
class Phone (models.Model):
    name = models.CharField(verbose_name="Модель", max_length=50)
    os = models.CharField(verbose_name="Операционная система", max_length=50)
    price = models.CharField(verbose_name="Стоимость", max_length=50)
    ram = models.IntegerField(verbose_name="Оперативная память")
    pixel = models.IntegerField(verbose_name="Число пикселей на дюйм")
    duble_camera = models.BooleanField(verbose_name="Двойная камера", null=True)
    processor = models.CharField(verbose_name="Процессор", max_length=50)
    screen = models.CharField(verbose_name="Разрешение экрана", max_length=50)
    fm = models.BooleanField(verbose_name="FM-радио", null=True)


class Xiomi(models.Model):
    name = models.ForeignKey(Phone, on_delete=models.CASCADE)
    extra = models.CharField(verbose_name="Дополнительно", max_length=200)
    def __str__(self):
        return self.name.name

class Iphone(models.Model):
    name = models.ForeignKey(Phone, on_delete=models.CASCADE)
    extra = models.CharField(verbose_name="Дополнительно",max_length=200)
    def __str__(self):
        return self.name.name 

class Sumsung(models.Model):
    name = models.ForeignKey(Phone, on_delete=models.CASCADE)
    extra = models.CharField(verbose_name="Дополнительно", max_length=200)
    def __str__(self):
        return self.name.name


