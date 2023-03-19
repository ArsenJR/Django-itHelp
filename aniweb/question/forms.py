from .models import Questions
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['title', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Формулировка вопроса'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст вопроса'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }