""" Contiene las funciones verificacionUser 
                            verificacionPass """


def verificacionUser(nom_usuario):
    """Verifica que la cuenta de usuario sea valida"""
    """La cuenta de usuario solo puede contener:
    -    caracteres alfanumericos
    -    '-', '_' o '.'                        """
    nom_usuario = str(nom_usuario)
    nom_usuario = nom_usuario.strip()
    nom_usuario = nom_usuario.lower()
    car_validos = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'

    for indice in nom_usuario:
        if(car_validos.find(indice) == -1):
            print('Su nombre de usuario contiene un caracter no valido:',
                  "'", indice, "'")
            return False
    return True


def verificacionPass(contrasena):
    """Verifica que la contraseña ingresada sea valida"""
    contrasena = str(contrasena)

    if not (contrasena):
        print('La contrasena esta vacia ')
        return False

    if contrasena.count(' ') != 0:
        print('La contrasena tiene espacios')
        return False

    contrasena = contrasena.lower()
    car_validos = 'abcdefghijklmnopqrstuvwxyz0123456789-_.?!@#$%^&*()'
    for indice in contrasena:
        if(car_validos.find(indice) == -1):
            print('Su contrasena contiene un caracter no valido:',
                  "'", indice, "'")
            return False
    return True


