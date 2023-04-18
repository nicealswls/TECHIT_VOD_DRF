from rest_framework import serializers #rest_framework에서 serializers 기능 임포트
from products.models import Product #products.models에 정의했던 Product 클래스 임포트


#위에서 임포트한 것들을 이용하여 파이썬 객체를 Json 형태로 바꾸도록 코드를 짤 것임
class ProductSerializer(serializers.ModelSerializer): #serializers에 있는 ModelSerializer를 상속받아 구현

    #Meta 클래스를 열어서 어떤 데이터를 Json으로 변환할지 명시
    class Meta: 

        model = Product #Product라는 클래스를 모델로 삼아 변환할 것이라는 뜻
        #fields는 0001_initial.py의 fields 내용을 참고하여 작성
        fields = (  #어떤 필드에 대해 Json으로 변환할 것인지 명시하는 곳
            'id',
            'product_name',
            'price'
        )
