from django.urls import path
from . import views

urlpatterns = [
  # path('', views.index),
  # path('<int:question_id>/', views.detail)

  # Generic View
  path('', views.IndexView.as_view()),
  path('<int:pk>/', views.DetailView.as_view())
]