from django.db import models

# Create your models here.
class Deposit(models.Model):
    fin_prdt_cd = models.CharField(max_length=255, primary_key=True)    # 금융상품 코드
    fin_co_no = models.CharField(max_length=255)                        # 금융회사 코드
    dcls_month = models.CharField(max_length=6)                         # 공시 제출월 yyyymm
    kor_co_nm = models.CharField(max_length=255)                        # 금융회사 명
    fin_prdt_nm = models.CharField(max_length=255)                      # 금융 상품명
    join_way = models.TextField()                                       # 가입 방법
    mtrt_int = models.TextField()                                       # 만기 후 이자율
    spcl_cnd = models.TextField()                                       # 우대조건
    join_deny = models.IntegerField()                                   # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member = models.TextField()                                    # 가입대상
    etc_note = models.TextField()                                       # 기타 유의사항
    max_limit = models.IntegerField(null=True)                          # 최고한도
    dcls_strt_day = models.CharField(max_length=8)                      # 공시 시작일 yyyymmdd
    dcls_end_day = models.CharField(max_length=8, blank=True, null=True) # 공시 종료일 yyyymmdd
    fin_co_subm_day = models.CharField(max_length=12)                   # 금융회사 제출일 yyyyddMMhhmm


class DepositOption(models.Model):
    product = models.ForeignKey("Deposit", on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=20)                    # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=20)                 # 저축 금리 유형명
    save_trm = models.CharField(max_length=10)                          # 저축 기간 [단위: 개월]
    intr_rate = models.FloatField()                                     # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField()                                    # 최고 우대금리 [소수점 2자리]


class Saving(models.Model):
    fin_prdt_cd = models.CharField(max_length=255, primary_key=True)    # 금융상품 코드
    fin_co_no = models.CharField(max_length=255)                        # 금융회사 코드
    dcls_month = models.CharField(max_length=6)                         # 공시 제출월 yyyymm
    kor_co_nm = models.CharField(max_length=255)                        # 금융회사 명
    fin_prdt_nm = models.CharField(max_length=255)                      # 금융 상품명
    join_way = models.TextField()                                       # 가입 방법
    mtrt_int = models.TextField()                                       # 만기 후 이자율
    spcl_cnd = models.TextField()                                       # 우대조건
    join_deny = models.IntegerField()                                   # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member = models.TextField()                                    # 가입대상
    etc_note = models.TextField()                                       # 기타 유의사항
    max_limit = models.IntegerField(null=True)                          # 최고한도
    dcls_strt_day = models.CharField(max_length=8)                      # 공시 시작일 yyyymmdd
    dcls_end_day = models.CharField(max_length=8, blank=True, null=True) # 공시 종료일 yyyymmdd
    fin_co_subm_day = models.CharField(max_length=12)                   # 금융회사 제출일 yyyyddMMhhmm


class SavingOption(models.Model):
    product = models.ForeignKey("Saving", on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=20)                    # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=20)                 # 저축 금리 유형명
    rsrv_type = models.CharField(max_length=20)                         # 적립 유형
    rsrv_type_nm = models.CharField(max_length=20)                      # 적립 유형명
    save_trm = models.CharField(max_length=10)                          # 저축 기간 [단위: 개월]
    intr_rate = models.FloatField()                                     # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField()                                    # 최고 우대금리 [소수점 2자리]
