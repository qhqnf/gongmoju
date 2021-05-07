from django.db import models
from django.conf import settings

class Ipo(models.Model):
    class Meta:
        db_table = "ipo"
        ordering = ["-company_code"]

    company_code = models.CharField(max_length=32, primary_key=True)
    company_name = models.CharField(max_length=32)
    start_date = models.DateField() # 청약 공고일
    payment_date = models.DateField()
    max_price_band = models.IntegerField()
    min_price_band = models.IntegerField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name

class SecurityCompany(models.Model):
    class Meta:
        db_table = "ipo_security_company"
        ordering = ["-ipo"]

    ipo = models.ForeignKey("Ipo", on_delete=models.CASCADE, related_name="security_company_set")
    company_name = models.CharField(max_length=32)
    stock_amount = models.IntegerField()

    def __str__(self):
        name = f"[{self.ipo}] {self.company_name}"
        return name

class IpoException(models.Model):
    class Meta:
        db_table = "ipo_exception"

    company_code = models.CharField(max_length=32)
    company_name = models.CharField(max_length=32)

    def __str__(self):
        return self.company_name
