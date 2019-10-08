import funciones


nuevo_usuario = input('Ingrese su nombre de usuario: \n')
funciones.verificacionUser(nuevo_usuario)

f = open('userDB.txt', 'r')
textoRaw = f.read()
usuarios = textoRaw.splitlines()

existe = False
for n in range(len(usuarios)):
    if usuarios[n].find(nuevo_usuario) != -1:
        print('El usuario ya existe')
        existe = True

nueva_contrasena = input('Ingrese su contrasena: \n')
funciones.verificacionPass(nueva_contrasena)


if existe == False:
    f = open('userDB.txt', 'a')
    f.write('('+nuevo_usuario+','+nueva_contrasena+')\n')


print('Fin')
# f.write('('+nuevo_usuario+','+nueva_contrasena+')\n')
# print(a)
