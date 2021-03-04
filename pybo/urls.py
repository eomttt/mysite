from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
  # Generic View
  # path('', views.IndexView.as_view(), name='index'),
  # path('<int:pk>/', views.DetailView.as_view(), name='detail'),

  path('', views.index, name='index'),
  path('<int:question_id>/', views.detail, name='detail'),
  path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
  path('question/create/', views.question_create, name='question_create'),
  path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
  path('question/delete/<int:question_id>/', views.question_delete, name='question_delete')
]