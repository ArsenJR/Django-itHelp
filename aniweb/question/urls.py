from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_home, name='question_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.QuestionsDetailView.as_view(), name='questions-detail')
]