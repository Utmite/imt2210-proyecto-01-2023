from os import path

def cn(cadena):
    try:
        valor = float(cadena)  
        if valor.is_integer():
            return int(valor)  
        else:
            return valor  
    except ValueError:
        return cadena 
x = path.join(
        path.dirname(path.abspath(__file__)),
        "db/Costos_producción.csv"
)
with open(x) as archivo:
    costos = archivo.readlines()
    costos = list(map(lambda x: x.strip().split(","), costos))
    costos = list(map(lambda x: [cn(x[0]), cn(x[1]), cn(x[2])], costos))
x = path.join(
        path.dirname(path.abspath(__file__)),
        "db/movies.csv"
)
with open(x) as archivo:
    pelis = archivo.readlines()
    pelis = list(map(lambda x: x.strip().split(","), pelis))
    pelis = list(map(lambda lista: list(map(cn, lista)), pelis))
x = path.join(
        path.dirname(path.abspath(__file__)),
        "db/ratings.csv"
)
with open(x) as archivo:
    ratings = archivo.readlines()
    ratings = list(map(lambda x: x.strip().split(","), ratings))
    ratings = list(map(lambda lista: list(map(cn, lista)), ratings))
x = path.join(
        path.dirname(path.abspath(__file__)),
        "db/Recursos_new.csv"
)
with open(x) as archivo:
    recursos_new = archivo.readlines()
    recursos_new = list(map(lambda x: x.strip().split(","), recursos_new))
    recursos_new = list(map(lambda lista: list(map(cn, lista)), recursos_new))
x = path.join(
        path.dirname(path.abspath(__file__)),
        "db/Recursos.csv"
)
with open(x) as archivo:
    recursos = archivo.readlines()
    recursos = list(map(lambda x: x.strip().split(","), recursos))
    recursos = list(map(lambda lista: list(map(cn, lista)), recursos))


