# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accuracy',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='timestamp')),
                ('weapon_type', models.CharField(max_length=200)),
                ('weapon_accuracy', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='lastSession',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='timestamp')),
                ('name', models.CharField(max_length=200)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('steam64', models.CharField(max_length=17)),
            ],
        ),
        migrations.AddField(
            model_name='lastsession',
            name='userID',
            field=models.ForeignKey(to='csc.user'),
        ),
        migrations.AddField(
            model_name='accuracy',
            name='userID',
            field=models.ForeignKey(to='csc.user'),
        ),
    ]
