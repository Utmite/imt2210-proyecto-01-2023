from typing import Dict
from clases import Vec
from archivos import costos, pelis, ratings, recursos, recursos_new

usuarios_vecs = {}
for user_id, movie_id, rating in ratings[1:]:
    x = Vec(["movie_id", "rating"], {"movie_id": movie_id, "rating": rating })
    usuarios_vecs[user_id] = x 

pelis_vecs = {}

for movie_id, *movie_name in pelis[1:]:
    x = Vec(["movie_id", "movie_name"], {"movie_id": movie_id, "movie_name": "".join(movie_name) })
    pelis_vecs[movie_id] = x

def sim(v: Vec, u: Vec):
    return (v.dot(u)) / (
        ( (v.dot(u)**1/2)*(v.dot(u)**1/2) )
    )

