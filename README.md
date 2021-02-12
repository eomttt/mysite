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

`$ from pybo.models import Question, Answer`

`$ from django.utils import timezone`

`$ q = Question(subject='Subject', content='Content', created_date=timezone.now())`

`$ q.save()`