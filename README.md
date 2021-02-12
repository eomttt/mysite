## 예제
[점프 투 장구](https://github.com/pahkey/djangobook)

## Installation
- vscode 를 사용하는 경우 Python, Pylance Extension 을 설치 한 후
- .vscode/settings.json 파일에서 가상환경 python path를 설정해주어야한다.
```json
{
  "python.pythonPath": "/Users/hyuntaeeom/Projects/personal/DjangoProject/venv_web/bin/python3"
}
```

## Data Make
1. Open django shell

`$ python manage.py shell`

2. Make Question data

```sh
>> from pybo.models import Question, Answer
>> from django.utils import timezone
>> q = Question(subject='Subject', content='Content', created_date=timezone.now())
>> q.save()
```

3. Linked Answer data [연결모델명_set]

- Answer model 에는 question field 가 들어있어서 a.question 등으로 쉽게 Question model를 찾을 수 있다. 그렇다면 반대는??

Django 에서는 반대 역시 쉽게 찾을 수 있는데 **연결모델명_set** 방법으로 찾을 수 있다.

```py
q.answer_set.all()
# <QuerySet [<Answer: Answer object (1)>]>
```

* 질문과 답변이 달리는 게시판을 상식적으로 생각해 보면 질문 1 개에는 1개 이상의답변이 달릴 수 있으므로 질문에 달린 답변은 q.answer_set 으로 조회해야 한다(답변세트를 조회). 답변은 질문 1개에 대한 것이므로 애초에 여러 개의 질문을 조회할 수 없다. 다시 말해 답변 1개 입장에서는 질문 1개만 연결되어 있으므로 a.question만 실행할 수 있다.
