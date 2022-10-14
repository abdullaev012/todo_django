from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')

class Delete(models.Model):    
    deleted_title = models.CharField(max_length = 50, verbose_name='Название')
    deleted_description = models.TextField(verbose_name='Описание')
    deleted_sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')

class Elected(models.Model):
    elected_title = models.CharField(max_length = 50, verbose_name='Название')
    elected_description = models.TextField(verbose_name='Описание')
    elected_sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')