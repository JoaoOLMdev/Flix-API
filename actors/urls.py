from django.urls import path
from actors.views import ActorlistCreateView, ActorRetrieveUpdateDestroyView


urlpatterns = [
    path('actors/', ActorlistCreateView.as_view(),name='actors-list-create'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(),name='actors-detail-view'),
]