from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter
from tests.views import test_page, poll_view,  PollView, api_questions, api_score, score_view


router = SimpleRouter()

router.register('api/polls', PollView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('users/', include('users.urls')),
    path('tests/', test_page, name='all-polls'),
    path('tests/<int:pk>/', poll_view, name='poll-view'),
    path('api/<int:pk>', api_questions, name='api-questions'),
    path('api/score', api_score, name='get-score'),
    path('tests/score', score_view, name='score-view'),
]

urlpatterns += router.urls
