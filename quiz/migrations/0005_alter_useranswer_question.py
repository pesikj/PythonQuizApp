# Generated by Django 5.0 on 2023-12-25 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_useranswer_admin_feedback_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='quiz.question'),
        ),
    ]
