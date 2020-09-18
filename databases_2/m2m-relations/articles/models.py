from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Sections(models.Model):
    title = models.ManyToManyField(Article, through='Relationship')
    section = models.CharField(max_length=50, verbose_name="Раздел")
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделов'

    def __str__(self):
        return self.section


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    sections = models.ForeignKey(Sections, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной раздел', default=False)

    def __str__(self):
        return '{0}_{1}'.format (self.article, self.sections)