from django.db import models

class Questions(models.Model):
    title = models.CharField('Вопрос', max_length=50)
    full_text = models.TextField('Текст вопроса')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'



