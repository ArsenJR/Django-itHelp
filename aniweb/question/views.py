from django.shortcuts import render, redirect
from .models import Questions
from .forms import QuestionsForm
from django.views.generic import DetailView, ListView

def question_home(request):
    questions = Questions.objects.order_by('-date')
    return render(request, 'question/question_home.html', {'questions': questions})


class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'question/detail_view.html'
    context_object_name = 'question'

def create(request):
    error = ''
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверно заполнены данные'

    form = QuestionsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'question/create.html', data)