import funciones


nuevo_usuario = input('Ingrese su nombre de usuario: \n')
funciones.verificacionUser(nuevo_usuario)

f = open('userDB.txt', 'r')
textoRaw = f.read()
usuarios = textoRaw.splitlines()
for n in range(len(usuarios)):
    usuarios[n] = usuarios[n].split(',')


existe = False
for n in range(len(usuarios)):
    if usuarios[n][0] == nuevo_usuario:
        print('El usuario ya existe')
        existe = True
        contrasena = input('Ingrese su contrasena: \n')
        funciones.verificacionPass(contrasena)
        if usuarios[n][1] == contrasena:
            print('La contrasena ingresada es correcta')
        else:
            print('La contrasena ingresada es incorrecta')


if (not existe):
    print('El usuario no existe, se creara una cuenta nueva\n')
    contrasena_nueva = input('Ingrese contrasena nueva:\n')
    if funciones.verificacionPass(contrasena_nueva):
        print('Creando nuevo User.')
        f = open('userDB.txt', 'a')
        f.write(nuevo_usuario+','+contrasena_nueva+'\n')
    else:
        print('Contrasena no valida.')


print('-'*10, ' Fin ', '-'*10)
# f.write('('+nuevo_usuario+','+nueva_contrasena+')\n')
# print(a)
