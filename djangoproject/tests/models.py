from django.db import models
from django.conf import settings


class Poll(models.Model):
    title = models.CharField(max_length=256)
    topic = models.CharField(max_length=256)
    number_of_questions = models.IntegerField()

    def __str__(self):
        return f"{self.title}-{self.topic}"


class Question(models.Model):
    question = models.CharField(max_length=256, default="question")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option_one = models.CharField(max_length=256, default="var")
    option_two = models.CharField(max_length=256, default="var")
    option_three = models.CharField(max_length=256, blank=True)
    correct = models.CharField(max_length=256, default="correct")
    marks = models.IntegerField(default=5)

    def __str__(self):
        return f"Вопрос: {self.question}, ответ: {self.correct}"


class Result(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    score = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)
