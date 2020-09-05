from django.db import models

# Create your models here.


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
