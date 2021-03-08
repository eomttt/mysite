from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from ..models import Question
from ..form import QuestionForm

@login_required(login_url='common:login')
def question_create(request):
  if request.method == 'POST':
    form = QuestionForm(request.POST)
    if (form.is_valid()):
      question = form.save(commit=False)
      question.author = request.user
      question.create_date = timezone.now()
      question.save()
      return redirect('pybo:index')
  else:
    form = QuestionForm()
  
  context = { 'form': form }
  return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
  question = get_object_or_404(Question, pk=question_id)

  if request.user != question.author:
    messages.error(request, 'Not have authorization.')
    return redirect('pybo:detail', question_id=question.id)
  
  if request.method == 'POST':
    form = QuestionForm(request.POST, instance=question)
    if form.is_valid():
      question = form.save(commit=False)
      question.modify_date = timezone.now()
      question.save()
      return redirect('pybo:detail', question_id=question.id)
  else:
    form = QuestionForm(instance=question)
  
  context = { 'form': form }
  return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  
  if request.user != question.author:
    messages.error(request, 'Not have authorization.')
  else:
    question.delete()
  
  return redirect('pybo:index')