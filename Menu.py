from Input import *
from Funciones import *
from Prints import *

def elegir_menu(max:int) -> int:
    """Solicita al usuario que elija una opcion del menu y la valida.
    """
    num = ingresar_entero_rango(
        "Elija una opcion: ",
        "Error, debe elegir una opcion valida",
        maximo = max,
        minimo = 1
    )
    return num

def iniciar_menu():
    while True:
        mostrar_menu_inicio()
        opcion = elegir_menu(2)
        if opcion == 2:
            print("Saliendo del sistema...")
            break

        usuario_logueado = iniciar_sesion()
        if usuario_logueado is None:
            print("Usuario o contraseña incorrectos.")
        else:
            match usuario_logueado["tipo"]:
                case "Cliente":
                    iniciar_menu_cliente(usuario_logueado)
                case "Restaurante":
                    iniciar_menu_restaurante(usuario_logueado)  #Inicia Menu del Rol Restaurante
                case "Administrador":
                    iniciar_menu_admin(usuario_logueado)        #Inicia Menu del Rol administrador

def iniciar_menu_cliente(cliente:dict) -> None:
    while True:
        mostrar_menu_cliente()
        eleccion = elegir_menu(3)
        match eleccion:
            case 1:
                ver_datos(cliente)
            case 2:
                realizar_pedido(cliente)
            case 3:    
                print("Saliendo del sistema...")
                break
                    
        input("\nPresione Enter para continuar...")

def iniciar_menu_restaurante(restaurante:dict) -> None:
    """Muestra y controla el menu de opciones para un usuario de tipo Restaurante."""
    while True:
        mostrar_menu_restaurante()
        eleccion = elegir_menu(3)
        match eleccion:
            case 1:
                ver_datos(restaurante)
            case 2:
                ver_pedidos_restaurante(restaurante)
            case 3:
                print("Saliendo del sistema...")
                break

        input("\nPresione Enter para continuar...")

def iniciar_menu_admin(admin:dict) -> None:
    """Muestra y controla el menu de opciones para un usuario de tipo Administrador."""
    while True:
        mostrar_menu_administrador()
        eleccion = elegir_menu(4)
        match eleccion:
            case 1:
                ver_datos(admin)
            case 2:
                listar_usuarios()
            case 3:
                eliminar_usuario()
            case 4:
                print("Saliendo del sistema...")
                break

        input("\nPresione Enter para continuar...")