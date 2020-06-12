from django.urls import path
from .views import *
# import 할 때, 아스타링크는 페이지와 관련없는 것도 전부 임포트하기에
# 아래처럼 필요한 것만 임포트해주는 것이 좋음
# from .views import BookmarkListView, BookmarkCreateView

urlpatterns = [
    path("", BookmarkListView.as_view(), name='list'),
    # config.urls.py에 bookmark/ 로 / 뒤에 아무 정보도 없으니 여기 경로는 공백
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    # <int:pk> : int는 컨버터라 부르는 기능이며 클래스 형태
    # 뒤쪽은 컨버터를 통해 반환받은 값 혹은 패턴에 일치하는 값의 변수명
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]