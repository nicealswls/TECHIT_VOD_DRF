from django.db import models

class Product(models.Model):
    #상품의 이름 지정 #blank는 빈칸 허용 여부 #defalut는 기본값
    product_name = models.CharField(max_length=30, blank=False , default='')
    #상품의 가격 지정 
    price = models.DecimalField(max_digits=20, decimal_places=1, blank=False, default=0)
                               #max_digits는 총 자릿수 결정, decimal_places는 소숫점 자릿수 결정
