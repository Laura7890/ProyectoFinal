import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

class CatalogoPelicula:
    def __init__(self, nombre_catalogo):
        self.nombre = nombre_catalogo
        self.ruta_archivo = f"{self.nombre}.txt"
        # Si el archivo no existe, lo creamos
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                pass  # Crear un archivo vacío
            print(f"Catálogo '{self.nombre}' creado exitosamente.")
        else:
            print(f"Catálogo '{self.nombre}' cargado exitosamente.")

    def agregar(self, pelicula):
        with open(self.ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(pelicula.get_nombre() + '\n')
        print(f"Película '{pelicula.get_nombre()}' agregada al catálogo.")

    def listar(self):
        if not os.path.exists(self.ruta_archivo):
            print("El catálogo no existe.")
            return
        with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
            peliculas = archivo.readlines()
            print(f"DEBUG: Se encontraron {len(peliculas)} películas en el archivo.")
            if not peliculas:
                print("No hay películas en el catálogo.")
                return
            print("\nPelículas en el catálogo:")
            for idx, pelicula in enumerate(peliculas, start=1):
                print(f"{idx}. {pelicula.strip()}")

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"Catálogo '{self.nombre}' eliminado.")
        else:
            print("El catálogo no existe.")

def main():
    print("Bienvenido al Gestor de Catálogo de Películas")
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ").strip()
    if not nombre_catalogo:
        print("El nombre del catálogo no puede estar vacío. Se usará 'DefaultCatalogo'.")
        nombre_catalogo = "DefaultCatalogo"
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True:
        print("\nMenú de Opciones:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar Catálogo de Películas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == '1':
            nombre_pelicula = input("Ingrese el nombre de la película: ").strip()
            if nombre_pelicula:
                pelicula = Pelicula(nombre_pelicula)
                catalogo.agregar(pelicula)
            else:
                print("El nombre de la película no puede estar vacío.")
        elif opcion == '2':
            catalogo.listar()
        elif opcion == '3':
            confirmacion = input(f"¿Está seguro de eliminar el catálogo '{nombre_catalogo}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                catalogo.eliminar()
                print("Programa finalizado.")
                break  # Salimos del programa después de eliminar el catálogo
            else:
                print("Eliminación cancelada.")
        elif opcion == '4':
            print("Gracias por usar el Gestor de Catálogo de Películas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()