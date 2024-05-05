import requests
import json


class MovieRecommender:
    def movie_recommender(self, movie_id, count=5):
        data = {}

        url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZDUxNTY3NGE1NWI2OWViZmI1OWNlNjI4NzQxYzM0NiIsInN1YiI6IjY1MjAwNzM5MDcyMTY2MDBlMmQ5M2RhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c2U37Zp6Up2G0U_Jx3VJGA4GI9V7JloiR-Vt2vm-XiI"
        }

        response = requests.get(url, headers=headers)
        if "results" not in response.json():
            data["error_message"]="Not a valid movie/movie_id. Try other movie."
            return data
        data["movie_recommended"] = []
        for movie in response.json()["results"]:
            movie_data = {
                "movie_id": movie['id'],
                "title": movie['original_title']
            }
            data["movie_recommended"].append(movie_data)

        data['movie_recommended'] = data['movie_recommended'][:count]
        return data
