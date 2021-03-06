# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TProductInfo(models.Model):
    productname = models.CharField(db_column='productName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='productCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    commenttime = models.CharField(db_column='commentTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_info'


class TProductComments(models.Model):
    productcode = models.CharField(db_column='productCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(max_length=2000, blank=True, null=True)
    commenttime = models.CharField(db_column='commentTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    commentdate = models.CharField(db_column='commentDate', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_comments'


class TClnProductInfo(models.Model):
    productcode = models.CharField(db_column='productCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(max_length=2000, blank=True, null=True)
    commenttime = models.CharField(db_column='commentTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sentiments = models.CharField(max_length=1, blank=True, null=True)
    commentdate = models.CharField(db_column='commentDate', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_cln_product_info'
