# Generated by Django 5.0.3 on 2024-03-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='materia_tarefa',
            new_name='materia_trabalho',
        ),
        migrations.RenameField(
            model_name='homework',
            old_name='nome_tarefa',
            new_name='nome_trabalho',
        ),
        migrations.AddField(
            model_name='homework',
            name='tipo_trabalho',
            field=models.IntegerField(choices=[(1, 'Prova'), (2, 'Tarefa')], default=2),
        ),
    ]
