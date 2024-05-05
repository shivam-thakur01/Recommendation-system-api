from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .movie_recommendation import MovieRecommender


class CreateUserView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        if not User.objects.filter(username=username).exists():
            # User does not exist, create a new user
            user = User.objects.create_user(username=username, password=password)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # User already exists
            return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)


class RecommendMovieV1(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        movie_id = request.data.get('movie_id')
        if request.data.get('movie_count'):
            movie_count = int(request.data.get('movie_count'))
        else:
            movie_count = 5
        data = {}
        user = authenticate(request, username=username, password=password)
        if not user:
            # User does not exist, throw error message
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            movie_recommender = MovieRecommender()
            recommended_movie = movie_recommender.movie_recommender(movie_id, movie_count)
            data.update(recommended_movie)
            return Response(data, status=status.HTTP_200_OK)
