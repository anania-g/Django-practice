# Generated by Django 4.0.5 on 2022-07-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_test',
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='question', max_length=200),
        ),
    ]
