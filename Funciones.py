from Input import *
from Prints import *
from Usuarios import *
from Productos import *

def agregar_elemento(elemento:any, lista:list) -> list:
    """Agrega un elemento al final de una lista (equivalente a append).
    Args:
        lista (list): lista a la que se agregará el elemento.
        elemento (any): elemento a agregar.
    Returns:
        list: lista con el elemento agregado.
    """
    lista[len(lista):] = [elemento]
    return lista

def iniciar_sesion():
    usuario_ingresado = pedir_nombre("Ingresar usuario: ", 4)
    contrasena_ingresada = pedir_contraseña("Ingresar contraseña: ")

    for u in usuarios:
        if u["usuario"] == usuario_ingresado and u["contrasena"] == contrasena_ingresada:
            return u
    return None

def realizar_pedido(cliente:dict) -> None:
    """Simula la realizacion de un pedido de comida y bebida por parte de un cliente.
    Al confirmar el pedido, actualiza la cantidad de pedidos y los puntos del cliente.
    Args:
        cliente (dict): cliente que esta realizando el pedido.
    """
    restaurante = pedir_nombre("Ingresar Restaurante: ", 3)

    mostrar_menu_comidas(comidas)
    num_comida = ingresar_entero_rango(
        "Elija un producto: ",
        "Error, debe elegir un producto correcto",
        maximo = 5,
        minimo = 1
    )
    cantidad_comida = ingresar_entero_rango(
        "Cuanto desea ordenar? ",
        "Error, debe elegir entre 1 y 15 unidades",
        maximo = 15,
        minimo = 1
    )

    mostrar_menu_bebidas(bebidas)
    num_bebida = ingresar_entero_rango(
        "Elija un producto: ",
        "Error, debe elegir un producto correcto",
        maximo = 4,
        minimo = 0
    )
    if num_bebida != 0:
        cantidad_bebida = ingresar_entero_rango(
            "Cuanto desea ordenar? ",
            "Error, debe elegir entre 1 y 15 unidades",
            maximo = 15,
            minimo = 1
        )
    else:
        cantidad_bebida = 0

    total_compra = (comidas[num_comida]["precio"] * cantidad_comida) + (bebidas[num_bebida]["precio"] * cantidad_bebida)
    confirmacion = input(f"Su total es de {total_compra}$ desea confirmar? (y/n): ")
    if confirmacion == "y":
        cliente["cantidad_pedidos"] += 1
        cliente["puntos"] += 10
        print(f"Gracias por comprar en {restaurante}, {cliente['nombre']}!")
        print(f"Sumaste 10 puntos. Ahora tenes {cliente['puntos']} puntos.")
    else:
        print("Pedido Cancelado.")

def ver_pedidos_restaurante(restaurante:dict) -> None:
    """Muestra un resumen simulado de la actividad de pedidos de un restaurante.
    Args:
        restaurante (dict): restaurante logueado del cual se muestran los pedidos.
    """
    print(f"El restaurante {restaurante['nombre_local']} recibio {restaurante['cantidad_pedidos']} pedidos en total.")
    print(f"Facturación mensual: ${restaurante['facturacion_mensual']}")

def listar_usuarios() -> None:
    """Muestra el usuario y el tipo de todos los usuarios registrados en el sistema."""
    print("=== Usuarios registrados ===")
    for u in usuarios:
        print(f"Usuario: {u['usuario']} - Tipo: {u['tipo']}")

def eliminar_usuario() -> None:
    """Solicita un nombre de usuario y lo elimina de la lista de usuarios, si existe."""
    usuario_a_eliminar = ingresar_cadena("Ingrese el nombre de usuario a eliminar: ")
    encontrado = False
    for u in usuarios:
        if u["usuario"] == usuario_a_eliminar:
            usuarios.remove(u)
            encontrado = True
            print(f"Usuario {usuario_a_eliminar} eliminado correctamente.")
            break
    if not encontrado:
        print("Usuario no encontrado.")