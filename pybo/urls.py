from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # 질문 클릭하면 해당 질문 페이지 이동
    path('<int:question_id>/', views.detail),
]