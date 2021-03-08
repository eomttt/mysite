from django import forms
from django.db.models import fields
from .models import Answer, Question, Comment

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['subject', 'content']

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = ['content']
  
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']