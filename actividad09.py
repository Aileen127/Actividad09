movies = []
while True:
    print("\n-- Bienvenido al catálogo de películas --")
    print("1. Ingresar una película")
    print("2. Mostrar las películas registradas")
    print("3. Buscar películas por género")
    print("4. Eliminar una película por título")
    print("5. Salir del programa")

    option = input("Ingresa una opción: ")

    # Inicio de match case
    match option:
        case "1":
            movie = []
            how_much_movies = int(input("Ingresa el número de cuantas películas deseas agregar, ingresa 0 si no quieres agregar más: "))
            while True:
                if how_much_movies > 0:
                    for how_much in how_much_movies:
                        new_movie = input("Ingresa la película por - Título (texto) / Año de estreno (número) / Género (texto, como por ejemplo: acción, drama, comedia, etc.): ")
                        movie.append(new_movie)

                    print("Se ha agregaddo la película correctamente")
                    break
                else:
                    print("")