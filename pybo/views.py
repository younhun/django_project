from django.shortcuts import render
from .models import Question
# Create your views here.
def index(request): 
    # 질문 목록 데이터 얻기
    # order_by는 정렬 -> (-기호가 있으면 내림차순, 없으면 오름차순)
    question_list = Question.objects.order_by('-create_date')
    # 딕셔너리 형태로 render
    context = {'question_list' : question_list}
    # 템플릿 파일을 작성하기 전에
    # 디렉토리 먼저 생성
    # config/settings.py 파일의 TEMPLATES 항목에 설정
    return render(request,'pybo/question_list.html',context)

def detatil(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)