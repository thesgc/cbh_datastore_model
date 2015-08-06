# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_hstore import hstore


class DataPoint(TimeStampedModel):
    created_by = models.ForeignKey("auth.User")
    project_data = hstore.SerializedDictionaryField() 
    supplementary_data = hstore.SerializedDictionaryField() 


class DataPointClassification(TimeStampedModel):
    created_by = models.ForeignKey("auth.User")
    project = models.ForeignKey("cbh_core_model.Project")
    description = models.CharField(max_length=1000, null=True, blank=True, default=None)
    l0 = models.ForeignKey(DataPoint, related_name='l0', null=True, blank=True, default=None)
    l1 = models.ForeignKey(DataPoint, related_name='l1',null=True, blank=True, default=None)
    l2 = models.ForeignKey(DataPoint, related_name='l2',null=True, blank=True, default=None)
    class Meta:
        unique_together = (('project','l0','l1','l2'))

