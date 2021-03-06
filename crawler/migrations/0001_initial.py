# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ingredient', models.CharField(max_length=1000)),
                ('Recipe', models.CharField(max_length=500)),
                ('Group', models.CharField(default='Ingredientes', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Way_Cooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=500)),
                ('Recipe', models.CharField(max_length=500)),
                ('Group', models.CharField(default='Modo de Fazer', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient_Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Word', models.CharField(max_length=500)),
                ('Count', models.IntegerField()),
                ('Type', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Palavras_Ignorar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Word', models.CharField(max_length=500)),
            ],
        ),
    ]
