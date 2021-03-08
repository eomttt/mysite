from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
  # Generic View
  # path('', views.IndexView.as_view(), name='index'),
  # path('<int:pk>/', views.DetailView.as_view(), name='detail'),

  path('', views.index, name='index'),
  # Question
  path('<int:question_id>/', views.detail, name='detail'),
  path('question/create/', views.question_create, name='question_create'),
  path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
  path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
  # Answer
  path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
  path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
  path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
  # Comment
  path('comment/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),
  path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
  path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),
  path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
  path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
  path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),
]