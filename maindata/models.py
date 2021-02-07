from django.db import models

# Create your models here.

class TestTable(models.Model):
    # city = models.CharField(max_length=30)
    # address = models.CharField(max_length=30)
    # add_pri = models.CharField(max_length=30)
    # add_sec = models.CharField(max_length=30)
    apt_name = models.CharField(max_length=30)
    sgmt = models.CharField(max_length=30)
    cnt_year_month = models.CharField(max_length=30)
    cnt_day = models.CharField(max_length=30)
    cnt_amt = models.CharField(max_length=30)
    level = models.CharField(max_length=30)

    def __str__(self):
        return self.apt_name

class Table2(models.Model):
    # city = models.CharField(max_length=30)
    # address = models.CharField(max_length=30)
    # add_pri = models.CharField(max_length=30)
    # add_sec = models.CharField(max_length=30)
    apt_code = models.CharField(max_length=10)
    apt_name = models.CharField(max_length=30)
    apt_addr = models.CharField(max_length=100)
    apt_born = models.CharField(max_length=30)
    apt_indvs = models.CharField(max_length=5)

    def __str__(self):
        return self.apt_name