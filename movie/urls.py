from django.urls import path
from .views import GenreAPIView, MovieAPIView

urlpatterns = [
    path('genre/', GenreAPIView.as_view(), name='genre-list-create'),
    path('movie/', MovieAPIView.as_view(), name='movie-list')
]