# Generated by Django 4.2.1 on 2023-06-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0008_category_message_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='categories',
            field=models.CharField(max_length=25),
        ),
    ]
