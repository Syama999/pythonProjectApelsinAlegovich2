from django.db import models
from django.urls import reverse
# Create your models here.

class Categories(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=100, verbose_name='Название', blank=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('j', kwargs={'category_id': self.pk})

class RealEstate(models.Model):
    id = models.IntegerField
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категория недвижимости')
    description = models.CharField(max_length=100, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    photo = models.ImageField(upload_to='photos/%Y/%M/%D', verbose_name='Фотография', blank=True)
    adress = models.CharField(max_length=100, verbose_name= 'Описание', blank = True)
    views = models.IntegerField(default = 0)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('h', kwargs={'pk': self.pk})






