from rest_framework.serializers import ModelSerializer
from .models import Poll, Question

class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id','title','topic','number_of_questions',]
