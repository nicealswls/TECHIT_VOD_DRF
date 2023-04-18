from rest_framework.viewsets import ModelViewSet #ViewSet 함수 임포트
from .serializer import ProductSerializer
from .models import Product


#API 구성
class ProductViewSet(ModelViewSet): #ModelViewSet 상속받음 -> ProductViewSet에서 ModelViewSet의 모든 기능 활용 가능
    #queryset: 어떤 모델을 다룰 것인지
    queryset = Product.objects.all()
    #serializer엔 우리가 만든 ProductSerializer를 넣는다
    serializer_class = ProductSerializer
