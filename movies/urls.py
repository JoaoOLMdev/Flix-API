from django.urls import path
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView, MoviestatsView


urlpatterns= [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    path('movies/stats', MoviestatsView.as_view(), name='movie-stats-view'),
]