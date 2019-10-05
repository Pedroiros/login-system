"""La cuenta de usuario solo puede contener:
    -    caracteres alfanumericos
    -    '-', '_' o '.'                        """


def verificacionUser(nom_usuario):
    """Verifica que la cuenta de usuario sea valida"""
    nom_usuario = str(nom_usuario)
    nom_usuario = nom_usuario.strip()
    nom_usuario = nom_usuario.lower()
    car_validos = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'

    for indice in nom_usuario:
        if(car_validos.find(indice) == -1):
            print('Su nombre de usuario contiene un caracter no valido:', "'", indice, "'")
            return False
    return True

if (verificacionUser ('pedro12#3')):
    print('Usuario valido')
else:
    print('Usuario no valido')

if (verificacionUser ('pedro123')):
    print('Usuario valido:')
else:
    print('Usuario no valido')