def leer_archivo(nombre_archivo):
    archivo = None
    try:
        # Intenta abrir el archivo en modo de lectura
        archivo = open(nombre_archivo, 'r')
        # Lee y muestra el contenido del archivo
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    
    except IOError:
        print("Error: No se pudo leer el archivo.")
    
    finally:
        # Asegura que el archivo se cierre independientemente de si ocurrió una excepción o no
        if archivo:
            archivo.close()
            print("Archivo cerrado.")

# Ejemplo de uso
nombre_archivo = input("Ingresa el nombre del archivo a leer: ")
leer_archivo(nombre_archivo)
