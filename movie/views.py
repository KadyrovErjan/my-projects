from getpass import GetPassWarning

from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import GenreSerializer
from .serializers import MovieSerializer
from .models import Genre, Rating, Movie





class GenreAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
class MovieAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
