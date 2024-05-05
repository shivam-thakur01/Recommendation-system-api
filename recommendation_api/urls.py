from django.urls import path
from .views import CreateUserView, RecommendMovieV1
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('create-user/', csrf_exempt(CreateUserView.as_view()), name='create-user'),
    path('movie-recommendation/', csrf_exempt(RecommendMovieV1.as_view()), name='movie-recommender'),
]
