# Generated by Django 4.1.7 on 2023-03-19 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_alter_questions_options_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='id_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answ', to='question.questions'),
        ),
    ]