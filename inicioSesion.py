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
        nroUser=(n)

nueva_contrasena = input('Ingrese su contrasena: \n')
funciones.verificacionPass(nueva_contrasena)

if existe and usuarios[nroUser][1] == nueva_contrasena:
    print('La contrasena ingresada es correcta')
else:
    print('La contrasena ingresada es incorrecta')

if (not existe) :
    print('Creando nuevo User.')
    f = open('userDB.txt', 'a')
    f.write(nuevo_usuario+','+nueva_contrasena+'\n')


print('Fin')
# f.write('('+nuevo_usuario+','+nueva_contrasena+')\n')
# print(a)
