# Generated by Django 5.1.2 on 2024-10-09 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Escolas_projeto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('escolaPertencente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Escolas_projeto.escola')),
            ],
        ),
    ]
