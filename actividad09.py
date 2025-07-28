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
        case "1": # Agregar
            movie = []

            while True:
                how_much_movies = int(input("Ingresa el número de cuantas películas deseas agregar: "))
                if how_much_movies > 0:
                    for how_much in range(how_much_movies):
                        new_movie = input("Ingresa la película por - Título (texto) / Año de estreno (número) / Género (texto, como por ejemplo: acción, drama, comedia, etc.): ")
                        movie.append(new_movie)
                        movies.append(movie) # Appendd lista principal
                    print("Se ha agregado la película correctamente")
                    break
                else:
                    print("Dato inválido, intenta de nuevo")
         #Mostrar peliculas
        case "2": #Mostrar peliculas
            print(f"Listado de películas actual: {movies}")
        case "3": # Buscar
            search = input("Ingresa el título de la película que deseas buscar: ").lower()
            if search in movie:
                print(f"La pelicula {search}, se encuentra agregada.")
            else:
                print("La película no se encuentra registrada.")
        case "4":
            print(f"Listado de películas actual: {movies}")
            delete = input("Ingresa el título de la película que deseas eliminar: ").lower()
            if delete in movie:
                movie.remove(delete)
                print("La película ha sido eliminada")
            else:
                print("La película no se encuentra en el listado")
        case "5":
            print("Ha salido del programa")
            break
        case _:
            print("Opción inválida, intente de nuevo")