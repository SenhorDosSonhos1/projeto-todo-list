# Generated by Django 4.2.6 on 2023-10-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=244)),
                ('data_inicio', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
            ],
        ),
    ]
