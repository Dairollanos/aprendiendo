# Generated by Django 3.1.3 on 2020-11-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('Nombre', models.CharField(max_length=100)),
                ('Salario', models.IntegerField()),
            ],
        ),
    ]
