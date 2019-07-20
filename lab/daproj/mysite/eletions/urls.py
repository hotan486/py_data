from django.conf.urls import url
from . import views

## 명시한 패턴 실제 뷰 페이지 로 이동 시키는 곳 
urlpatterns = [
	url(r'^$',views.index),
]
