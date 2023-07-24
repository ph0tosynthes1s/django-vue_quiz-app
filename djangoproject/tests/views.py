import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from .models import Poll, Question, Result
from .serializer import PollSerializer


def test_page(request):
    return render(request, 'tests/tests.html', {'obj': Poll.objects.all()})


class PollView(LoginRequiredMixin, ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    raise_exception = True


def api_questions(request, pk):
    all_questions = Question.objects.filter(poll=pk)
    questions = []

    for all_question in all_questions:
        options = []
        question = {}
        question['id'] = all_question.id
        question['question'] = all_question.question
        question['correct'] = all_question.correct
        options.append(all_question.option_one)
        options.append(all_question.option_two)
        if all_question.option_three != '':
            options.append(all_question.option_three)
        question['options'] = options

        questions.append(question)
    return JsonResponse(questions, safe=False)


def poll_view(request, pk):
    poll = Poll.objects.get(pk=pk)
    return render(request, 'tests/poll.html', {'obj': poll})


def get_absolute_url(self):
    return reverse('poll-view', kwargs={'poll_id': self.pk})


def score_view(request):
    author = request.user
    score = Result.objects.filter(author=author)
    context = {'score': score}
    return render(request, 'tests/score.html', context)


@csrf_exempt
def api_score(request):
    data = json.loads(request.body)
    user = request.user
    poll_id = data.get('poll_id')
    chooses = json.loads(data.get('data'))
    score = 0
    incorrect_answers = 0
    correct_answers = 0
    poll = Poll.objects.get(id=poll_id)
    for choose in chooses:
        question = Question.objects.get(id=choose.get('question_id'))
        if str(question.correct) == str(choose.get('option')):
            score = score + question.marks
            correct_answers += 1
        else:
            incorrect_answers += 1
    percent = (correct_answers / (incorrect_answers + correct_answers) * 100)
    score_board = Result(poll=poll, score=score, author=user, incorrect_answers=incorrect_answers,
                         correct_answers=correct_answers, percent=percent)
    score_board.save()
    return JsonResponse({'message': 'success'})
