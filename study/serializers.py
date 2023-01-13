from rest_framework import serializers
from .models import Students, Score




# student = Students.objects.get(pk=1).score_set

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    score_set = ScoreSerializer(many=True, read_only=True)
    class Meta:
        model = Students
        fields = ['name', 'address', 'email', 'score_set']
