from rest_framework import serializers
from .models import Search, Answer

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        #fields = ['search_id', 'sentence']
        fields = ['search_id','sentence','search_date']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer_id','search_id','answer']