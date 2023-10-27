from typing import Dict
from clases import Vec
from archivos import costos, pelis, ratings, recursos, recursos_new
from pprint import pprint

dominio = []
users = {}
movies = {}



for _, movie_id, rating in ratings[1:]:
    dominio.append(movie_id)

usuarios = set(map(lambda x: x[0], ratings[1:]))
for user_id in usuarios:

    usurio_rating = list(filter(lambda x: x[0] == user_id, ratings[1:]))

    movie_id2rating = dict(map(lambda x: (x[1], x[2]), usurio_rating))
    vector_gusto = Vec(dominio=dominio, coordenadas=movie_id2rating)

    users[user_id] = vector_gusto

peliculas = set(map(lambda x: x[1], ratings[1:]))
for movie_id in peliculas:
    movie_id_rating = list(filter(lambda x: x[1] == movie_id, ratings[1:]))
    usur_id2rating = dict(map(lambda x: (x[0], x[2]), movie_id_rating))

    vector = Vec(dominio=usuarios, coordenadas=usur_id2rating)
    movies[movie_id] = vector


def sim(v: Vec, u: Vec):
    return (v.dot(u)) / (
        ( ((u.dot(u))**1/2)*((v.dot(v))**1/2) )
    )

def vecinos(users: dict, user_id: int, k: int):
    _users = users.copy()

    del _users[user_id]

    w = list(map(lambda x: (x[0], sim(users.get(user_id), x[1])), _users.items()))
    w = dict(sorted(w, key=lambda x: x[1], reverse=True))

    return w[:k]

print("hola")
print(vecinos(users, 2, 10))


