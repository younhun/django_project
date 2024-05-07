from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm


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

def detail(request, question_id):
    # 없는 id를 찾으면 500에러 발생
    # 500(서버)에러 대신 404에러 발생하게끔 예외처리
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # request로 읽을 수 있다.
    # POST로 전송된 폼 데이터 항목 중 content 값을 가져온다.
    answer = Answer(question=question, content=request.POST.get('content'),
                    create_date = timezone.now())
    answer.save()
    # 답변을 생성 후, 질문 상세 화면을 '다시' 보여주기 위해 redirect 사용
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    # ***매우 중요***
    # GET, POST에 따라 다르게 처리
    # 2. 질문등록 화면에서 값을 입력하고 저장하기를 누르면 POST가 사용되어 아래 코드 실행
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid(): # 폼이 유효하다면
            question = form.save(commit=False) # 1. 폼에 저장된 데이터를 question객체에 저장, commit=False는 임시저장을 의미(실제 데이터베이스에 저장x)
            question.create_date = timezone.now() # 2. 시간 값 설정한 후
            question.save() # 3. 실제 데이터를 저장
            return redirect('pybo:index')
    # 1. 질문등록하기는 GET이 사용되어 else구문 실행
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request,'pybo/question_form.html',context)
    
