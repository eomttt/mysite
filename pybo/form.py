from django import forms
from django.forms import fields
from .models import Answer, Question

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['subject', 'content']

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = ['content']