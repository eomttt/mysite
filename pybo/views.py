from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from .models import Answer, Question

# Create your views here.
def index(request):
  question_list = Question.objects.order_by('-create_date')
  context = {'question_list': question_list}
  return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = {'question': question}
  return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
  question = get_object_or_404(Question, pk=question_id)

  # Save by question.answer_set
  # question.answer_set.create(content=request.POST.get('content', create_date=timezone.now()))
  answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
  answer.save()
  return redirect('pybo:detail', question_id=question_id)

# Generic View
class IndexView(generic.ListView):
  def get_queryset(self):
    return Question.objects.order_by('-create_date')

class DetailView(generic.DetailView):
  model = Question