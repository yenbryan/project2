# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_profilepicture_default_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
