import datetime

#Establecemos colores para ser usados luego en la consola y asi mostrar resultados en distinto colores
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
TERMINA_COLOR = '\033[0m'
NEGRITA = '\033[1m'
SUBRAYADO = '\033[4m'

#Establecemos los productos posibles para la venta, para esto creamos una lista de objectos
productos = ['Banana', 'Manzana', 'Peras']
#Establecemos los precios que van a tener cada uno de ellos, creamos otra lista en la cual pondremos los precios
#en el mismo orden que la lista de productos para que coincidan los indices
precios = [14.56, 21.45, 39.25]

#Definimos una funcion que nos liste los posibles productos a ser comprados
#De esta manera podemos reutilizar el codigo en caso de ser necesario
global indice_producto_seleccionado
global cantidad
def mostrarProductos():
    global indice_producto_seleccionado
    for i, opcion in enumerate(productos):
        #Imprimimos las posiblies opciones con un color para hacerlo mas user friendlly
        print(f'{AZUL}{i+1}. {opcion} - {AMARILLO}${precios[i]}{TERMINA_COLOR}')
    indice_producto_seleccionado = input('Seleccione el producto que desea: ')
    #Verificamos la eleccion, en caso de no ser crrecta, vamos a volver a mostrarle las opciones
    verificarEleccionDeProducto()

#Definimos una funcion para verificar la seleccion del usuario
def verificarEleccionDeProducto():
    global indice_producto_seleccionado
    if(indice_producto_seleccionado.isdigit() and 1 <= int(indice_producto_seleccionado) <= len(productos)):
        #El producto es correcto, pero en este punto el indice tiene un número mas debido a que lo listamos empezando del 1
        #Los arrays (listas) empiezan en 0, entonces vamos a corregir el indice quitandole 1 a la seleccion
        indice_producto_seleccionado = int(indice_producto_seleccionado) - 1;
        print(f'Producto Seleccionado: {AZUL}{productos[indice_producto_seleccionado]}{TERMINA_COLOR}')
    else:
        #En caso de que el producto no exista en nuestra lista, mostramos un error y volvemos a llamar a nuestra funcion
        #mostrarProductos() para que el usuario intente nuevamente
        print(f'{ROJO}El producto debe ser una opcion valida, vuelva a intentarlo{TERMINA_COLOR}')
        mostrarProductos()

#Definimos una funcion para permitir el ingreso de la cantidad
def indicarCntidadProductos():
    global cantidad
    cantidad = input('Por favor, indique la cantidad de productos: ')
    verificarCantidadProductos()

#Definimos una funcion para verificar la cantidad definida por el usuario
def verificarCantidadProductos():
    global cantidad
    if(not cantidad.isdigit() or int(cantidad) < 1):
        print(f'{ROJO}La cantidad parece no ser válida, vuelva a intentarlo{TERMINA_COLOR}')
        indicarCntidadProductos()

def imprimirFactura():
    global cantidad
    global indice_producto_seleccionado
    total = int(cantidad) * precios[indice_producto_seleccionado]
    precio_unitario = precios[indice_producto_seleccionado]
    producto_seleccionado = productos[indice_producto_seleccionado]

    print(f'\n{AMARILLO}--------------------------------------------------------------------------------------------------{TERMINA_COLOR}')
    print('{:50} {:>50}'.format(*[f'Fecha: {NEGRITA}{datetime.date.today()}{TERMINA_COLOR}', f'No.: {NEGRITA}00000001{TERMINA_COLOR}']))
    print('{:20} {:40} {:>20} {:>20}'.format(*[f'{AMARILLO}Cantidad{TERMINA_COLOR}', f'{AMARILLO}Producto{TERMINA_COLOR}', f'{AMARILLO}Precio{TERMINA_COLOR}', f'{AMARILLO}Subtotal{TERMINA_COLOR}']))
    print('{:20} {:40} {:>20} {:>20}'.format(*[f'{VERDE}{cantidad}{TERMINA_COLOR}', f'{VERDE}{producto_seleccionado}{TERMINA_COLOR}', f'{VERDE}${precio_unitario}{TERMINA_COLOR}', f'{VERDE}${total}{TERMINA_COLOR}']))
    print('{:>65} {:>20}'.format(*[f'{AMARILLO}Total: {TERMINA_COLOR}', f'{VERDE}${total}{TERMINA_COLOR}']))
    print(f'{AMARILLO}--------------------------------------------------------------------------------------------------{TERMINA_COLOR}')


#Llamamos al metodo que nos lista los productos
mostrarProductos()

#En este punto, el usuario selecciono un producto correcto, por lo que le pedimos que ingrese la cantidad
indicarCntidadProductos()

#Ya tenemos todos los parametros necesarios para mostrar la Facture al Usuario
#Solo nos resta Imprimir
imprimirFactura()












