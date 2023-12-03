import os
import json

def crear_usuario(usuarios):
    usuario = input("Ingrese el nombre de usuario: ")
    # Se controla el usuario y en caso de existir se pide que ingrese otro usuario
    while usuario in usuarios:
        print("El usuario ya existe.")
        usuario = input("Ingrese otro nombre de usuario: ")

    contrasena = input("Ingrese la contraseña: ")
    # Se controla que tenga la longitud solicitada y si no lo es, solicita que ingrese una correcta
    while len(contrasena) < 6 or len(contrasena) > 10:
        print("La contraseña debe tener entre 6 y 10 caracteres.")
        contrasena = input("Ingrese la contraseña: ")

    confirmacion = input("Confirme la contraseña: ")
    # Controla que ambas contraseñas sean iguales
    while contrasena != confirmacion:
        print("Las contraseñas no coinciden.")
        confirmacion = input("Confirme la contraseña: ")

    usuarios[usuario] = contrasena
    return usuarios

def iniciar_sesion(usuarios):
    usuario = input("Ingrese el nombre de usuario: ")
    if usuario not in usuarios:
        print("El usuario no existe.")
        return
    # Contrala que se ingrese correctamente la contraseña y en caso contrario retorna al menu 
    # luego de haber concluido las cantidad de veces que se podia ingresar la contraseña
    for i in range(3):
        contrasena = input("Ingrese la contraseña: ")
        if contrasena == usuarios[usuario]:
            print("Inicio de sesión exitoso!")
            return
        else:
            print("Contraseña incorrecta. Intentos restantes: ", 2-i)
    print("Demasiados intentos fallidos. Inténtalo de nuevo más tarde.")

##### Se guardan los usuarios creados tanto en .json como en .txt #####

def guardar_usuarios(usuarios):
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)
        
def guardar_usuarios_txt(usuarios):
    with open('usuarios.txt', 'w') as f:
        for usuario, contrasena in usuarios.items():
            f.write(f'{usuario}:{contrasena}\n')
            
#######################################################################

def cargar_usuarios():
    try:
        with open('usuarios.json', 'r', encoding='utf-8') as f:
            datos = json.load(f)
    except FileNotFoundError:
        datos = {}
    return datos


    
menu = """
*** Menú ***
1 - Crear Usuario
2 - Iniciar Sesion
3 - Salir
"""

opcion = ''

#### ESTRUCTURA PRINCIPAL ####
while opcion != '3':
    os.system('cls')
    print(menu)
    opcion = input('Su opción >>> ')
    usuarios = cargar_usuarios()
    if opcion == '1':
        usuarios = crear_usuario(usuarios)
        guardar_usuarios(usuarios)
        guardar_usuarios_txt(usuarios)
    elif opcion == '2':
        iniciar_sesion(usuarios)
    elif opcion == '3':
        print('Adiós!')
        continue 
    else:
        print('Opción inválida!')
    input('ENTER para continuar')
    