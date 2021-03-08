from django.core.paginator import Paginator
from django.views import generic
from django.shortcuts import render, get_object_or_404

from ..models import Answer, Comment, Question

def index(request):
  page = request.GET.get('page', '1')
  question_list = Question.objects.order_by('-create_date')

  paginator = Paginator(question_list, 10)
  page_obj = paginator.get_page(page)

  context = { 'question_list': page_obj }
  return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = { 'question': question }
  return render(request, 'pybo/question_detail.html', context)

# Generic View
class IndexView(generic.ListView):
  def get_queryset(self):
    return Question.objects.order_by('-create_date')

class DetailView(generic.DetailView):
  model = Question