# Generated by Django 5.0 on 2024-01-01 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_question_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order']},
        ),
    ]