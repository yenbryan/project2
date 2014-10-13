# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=125)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=125)),
                ('text', models.TextField()),
                ('category', models.ForeignKey(related_name=b'discussions', to='discussion.Category')),
                ('poster', models.ForeignKey(related_name=b'discussions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(related_name=b'comments', to='discussion.Discussion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(related_name=b'comments', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
