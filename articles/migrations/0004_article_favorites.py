# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_auto_20150609_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
