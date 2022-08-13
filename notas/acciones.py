import notas.nota as modulo


class Acciones:

    def crear (self, usuario):
        print(f'\n¡Ok {usuario[1]}, creemos una nueva nota!\n')

        titulo = input('Ingresa el titulo de la nota: ')
        descripcion = input('Ingresa la descripcion de la nota: ')

        nota = modulo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'\nGenial! Se a guardado correctamente tu nota: {nota.titulo}')
        else:
            print(f'\nLo siento {usuario[1]}, tu nota no se ha guardado!')

    def mostrar (self, usuario):
        print(f'\n{usuario[1]} aqui tienes tus notas:')

        nota = modulo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print('\n******************************\n')

            print(f'Titulo: {nota[2]}\n')
            print(f'Descripcion: {nota[3]}\n')

            print('******************************')

    def eliminar (self, usuario):

        print(f'\nGenial {usuario[1]}, borremos la nota\n')
        titulo = input('Introduce el titulo de la nota a borrar: ')

        nota = modulo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f'\nSe ha borrado correctamente la nota: {nota.titulo}')
        else:
            print('\nNo se borró la nota de forma correcta T_T')






























