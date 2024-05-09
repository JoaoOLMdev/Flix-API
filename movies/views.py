from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    