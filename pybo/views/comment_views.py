from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from ..models import Answer, Comment, Question
from ..form import CommentForm

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
  question = get_object_or_404(Question, pk=question_id)

  if request.method == 'POST':
    form = CommentForm(request.POST)
    if (form.is_valid()):
      comment = form.save(commit=False)
      comment.author = request.user
      comment.create_date = timezone.now()
      comment.question = question
      comment.save()
      return redirect('{}#comment_{}'.format(
          resolve_url('pybo:detail', question_id=comment.question.id), comment.id))
  else:
    form = CommentForm()

  context = { 'form': form }
  return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)

  if request.user != comment.author:
    messages.error(request, 'Not have authorization.')
    return redirect('pybo:detail', question_id=comment.question.id)
  
  if request.method == 'POST':
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.modify_date = timezone.now()
      comment.save()
      return redirect('{}#comment_{}'.format(
          resolve_url('pybo:detail', question_id=comment.question.id), comment.id))
  else:
    form = CommentForm(instance=comment)
  
  context = { 'form': form }
  return render(request, 'pybo/comment_form.html', context)
      
@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)
  
  if request.user != comment.author:
    messages.error(request, 'Not have authorization.')
  else:
    comment.delete()

  return redirect('pybo:detail', question_id=comment.question.id)

@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
  answer = get_object_or_404(Answer, pk=answer_id)

  if request.method == 'POST':
    form = CommentForm(request.POST)
    if (form.is_valid()):
      comment = form.save(commit=False)
      comment.author = request.user
      comment.create_date = timezone.now()
      comment.answer = answer
      comment.save()
      return redirect('{}#comment_{}'.format(
          resolve_url('pybo:detail', question_id=answer.question.id), comment.id))
  else:
    form = CommentForm()

  context = { 'form': form }
  return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)

  if request.user != comment.author:
    messages.error(request, 'Not have authorization.')
    return redirect('pybo:detail', question_id=comment.answer.question.id)
  
  if request.method == 'POST':
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.modify_date = timezone.now()
      comment.save()
      return redirect('{}#comment_{}'.format(
          resolve_url('pybo:detail', question_id=comment.answer.question.id), comment.id))
  else:
    form = CommentForm(instance=comment)
  
  context = { 'form': form }
  return render(request, 'pybo/comment_form.html', context)
      
@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)
  
  if request.user != comment.author:
    messages.error(request, 'Not have authorization.')
  else:
    comment.delete()

  return redirect('pybo:detail', question_id=comment.answer.question.id)
