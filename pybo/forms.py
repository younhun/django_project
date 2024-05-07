# 폼 생성하기
# 페이지 요청시 전달되는 파라미터들을 쉽게 관리하기 위해 사용하는 클래스
# 파라미터의 값이 누락되지 않았는지, 형식은 적절한지 등을 검증
from django import forms
from pybo.models import Question

# forms.ModelForm, forms.Form이 존재
# 모델과 연결된 폼으로 폼을 저장하기 위해 forms.ModelForm 사용 -> 반드시 이너 클래스인 Meta 반드시 필요
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # 질문 폼에서 사용할 질문 모델의 속성