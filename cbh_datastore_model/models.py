# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_hstore import hstore
from cbh_core_model.models import CustomFieldConfig





class DataPoint(TimeStampedModel):
    '''Holds data for one hierachical section of a dataset. 
    Data that is related to the given custom field config is stored in project_data'''
    custom_field_config = models.ForeignKey("cbh_core_model.CustomFieldConfig",
         help_text="The schema of this datapoint")
    created_by = models.ForeignKey("auth.User")
    project_data = hstore.SerializedDictionaryField(
        help_text="Data that is related to the given custom field config is stored in project_data as JSON") 
    supplementary_data = hstore.SerializedDictionaryField(
        help_text="Extra data that was uploaded but was not mapped to the project data") 



class DataPointClassificationPermission(TimeStampedModel):
    created_by = models.ForeignKey("auth.User")  
    project = models.ForeignKey("cbh_core_model.Project")
    data_point_classification = models.ForeignKey("cbh_datastore_model.DataPointClassificationPermission", related_name="l0_permission")





class DataPointClassification(TimeStampedModel):
    created_by = models.ForeignKey("auth.User")
    description = models.CharField(max_length=1000, null=True, blank=True, default=None)
    data_form_config = models.ForeignKey("cbh_core_model.DataFormConfig")
    l0 = models.ForeignKey(DataPoint, related_name='l0', null=True, blank=True, default=None)
    l1 = models.ForeignKey(DataPoint, related_name='l1',null=True, blank=True, default=None)
    l2 = models.ForeignKey(DataPoint, related_name='l2',null=True, blank=True, default=None)
    l3 = models.ForeignKey(DataPoint, related_name='l3',null=True, blank=True, default=None)
    l4 = models.ForeignKey(DataPoint, related_name='l4',null=True, blank=True, default=None)

    class Meta:
        unique_together = (('data_form_config','l0','l1','l2','l3','l4'))


