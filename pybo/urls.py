from django.urls import path

from . import views

# pybo 앱 하나만 사용중이지만 다른 앱이 프로젝트에 추가 될 수도 있다.
# 서로 다른 앱에서 동일한 url 별칭을 사용하면 중복이 발생한다.
app_name = 'pybo'


urlpatterns = [
    # url 별칭
    # url 링크의 구조가 자주 변경된다면 템플릿에서 사용한 모든 url을
    # 일일이 찾아가며 수정해야 하는 리스크 발생
    path('', views.index, name='index'),
    # 질문 클릭하면 해당 아이디를 갖는 질문 페이지 이동
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]