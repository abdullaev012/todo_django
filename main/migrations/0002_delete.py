# Generated by Django 4.1.1 on 2022-10-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_title', models.CharField(max_length=50, verbose_name='Название')),
                ('deleted_description', models.TextField(verbose_name='Описание')),
                ('deleted_sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')),
            ],
        ),
    ]