# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def create_default_datapoint(apps, b):
        try:
            User = apps.get_model("auth.User")
            User.objects.create(username=-1, id=-1)
        except:
            pass
        try:
            CFC = apps.get_model("cbh_core_model.CustomFieldConfig")
            CFC.objects.create(
                id=-1, created_by_id=-1, name="-1 default do not delete")
        except:
            pass
        try:
            DataPoint = apps.get_model("cbh_datastore_model.DataPoint")
            DataPoint.objects.all().delete()
            DataPoint.objects.create(
                custom_field_config_id=-1, created_by_id=-1, pk=1)
        except:
            pass
        try:
            DataPointClassification = apps.get_model(
                "cbh_datastore_model.DataPointClassification")
            DataPointClassification.objects.all().delete()
        except:
            pass

    dependencies = [
        ('cbh_datastore_model', '0010_auto_20150810_0917'),
    ]

    operations = [
        migrations.RunPython(create_default_datapoint),
    ]
