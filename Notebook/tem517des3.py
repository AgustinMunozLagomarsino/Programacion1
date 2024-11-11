import csv

def actualizar_copias(titulo_libro, nuevas_copias, archivo="inventario.csv"):
    try:
        inventario_actualizado = []
        libro_encontrado = False
        
        # Leer el archivo y actualizar la cantidad de copias si coincide el título
        with open(archivo, "r") as f:
            lector_csv = csv.reader(f)
            
            # Leer cada fila del archivo CSV
            for linea in lector_csv:
                titulo, copias = linea[0], linea[1]
                
                # Si encontramos el libro, actualizamos la cantidad de copias
                if titulo.lower() == titulo_libro.lower():
                    inventario_actualizado.append([titulo, str(nuevas_copias)])
                    libro_encontrado = True
                else:
                    inventario_actualizado.append(linea)
        
        # Mensaje si no se encuentra el libro
        if not libro_encontrado:
            print(f"El libro '{titulo_libro}' no se encontró en el inventario.")
            return
        
        # Escribir el archivo actualizado
        with open(archivo, "w", newline="") as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerows(inventario_actualizado)
        
        print(f"Las copias de '{titulo_libro}' se actualizaron a {nuevas_copias}.")

    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")

# Ejemplo de uso
titulo_libro = input("Ingrese el título del libro que desea actualizar: ")
nuevas_copias = int(input("Ingrese la nueva cantidad de copias: "))
actualizar_copias(titulo_libro, nuevas_copias)
