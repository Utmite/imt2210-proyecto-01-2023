
def cn(cadena):
    try:
        valor = float(cadena)  # Intenta convertir la cadena a un número flotante
        if valor.is_integer():
            return int(valor)  # Si es un número entero, conviértelo a entero
        else:
            return valor  # De lo contrario, devuelve el número flotante
    except ValueError:
        return cadena  # Si no se puede convertir, devuelve Non
    
with open("src/db/Costos_producción.csv") as archivo:
    costos = archivo.readlines()
    costos = list(map(lambda x: x.strip().split(","), costos))
    costos = list(map(lambda x: [cn(x[0]), cn(x[1]), cn(x[2])], costos))

with open("src/db/movies.csv") as archivo:
    pelis = archivo.readlines()
    pelis = list(map(lambda x: x.strip().split(","), pelis))
    pelis = list(map(lambda lista: list(map(cn, lista)), pelis))

with open("src/db/ratings.csv") as archivo:
    ratings = archivo.readlines()
    ratings = list(map(lambda x: x.strip().split(","), ratings))
    ratings = list(map(lambda lista: list(map(cn, lista)), ratings))

with open("src/db/Recursos_new.csv") as archivo:
    recursos_new = archivo.readlines()
    recursos_new = list(map(lambda x: x.strip().split(","), recursos_new))
    recursos_new = list(map(lambda lista: list(map(cn, lista)), recursos_new))

with open("src/db/Recursos.csv") as archivo:
    recursos = archivo.readlines()
    recursos = list(map(lambda x: x.strip().split(","), recursos))
    recursos = list(map(lambda lista: list(map(cn, lista)), recursos))


