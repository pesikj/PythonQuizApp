# Generated by Django 5.0 on 2024-01-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_question_max_attempts_alter_useranswer_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='missing_answer',
            field=models.IntegerField(default=0),
        ),
    ]
