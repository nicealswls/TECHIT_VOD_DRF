from django.urls import include, path #장고가 지원하는 url 모듈 임포트
from rest_framework.routers import DefaultRouter #Router: 간단하고 빠르게 자동으로 url 라우팅(네트워크들의 연결을 담당하는 라우터 장비가 데이터의 목적지를 확인하여 빠르고 정확한 길을 찾아 전달해 주는 것)을 할 수 있도록 해 주는 것, 여기서는 DRF가 지원하는 DefaultRouter를 사용할 것
from . import views #우리가 작성한 views.py 내용 임포트

#router 변수 생성
router = DefaultRouter()
#등록 - product와 views.ProductViewSet 간 경로를 연결하여 API를 요청을 주고받을 수 있도록 하는 코드
router.register('product', views.ProductViewSet) 

#urlpatterns을 리스트 형태로 입력
urlpatterns = [
    path('', include(router.urls)) #router에 지정된 경로 규칙을 포함한다
]