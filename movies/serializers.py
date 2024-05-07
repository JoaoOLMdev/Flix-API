from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate

        return None

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Resumo não deve ser maior do que 200 caracteres.")
        return value