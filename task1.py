from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Строковое поле с ограничением в 200 символов
    body = models.TextField(null=True, blank=True)  # Необязательное текстовое поле
    published = models.BooleanField(default=False)  # Булево поле со значением по умолчанию False
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматическое заполнение даты создания
    updated_at = models.DateTimeField(auto_now=True)  # Автоматическое обновление даты при изменении
