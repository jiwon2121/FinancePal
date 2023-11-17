from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    cur_unit = models.CharField(max_length=50, primary_key=True)
    ttb = models.CharField(max_length=50)
    tts = models.CharField(max_length=50)
    deal_bas_r = models.CharField(max_length=50)
    bkpr = models.CharField(max_length=50)
    yy_efee_r = models.CharField(max_length=50)
    ten_dd_efee_r = models.CharField(max_length=50)
    kftc_bkpr = models.CharField(max_length=50)
    kftc_deal_bas_r = models.CharField(max_length=50)
    cur_nm = models.CharField(max_length=50)