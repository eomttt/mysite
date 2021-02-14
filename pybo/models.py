from django.db import models

class Question(models.Model):
  subject = models.CharField(max_length=200)
  content = models.TextField()
  create_date = models.DateField()

  def __str__(self):
    return self.subject

class Answer(models.Model):
  # on_delete=models.CASCADE 는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField()

  def __str__(self):
    return self.content
