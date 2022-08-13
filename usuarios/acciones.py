import usuarios.usuario as user
import notas.acciones


class Acciones:

    def registro(self):

        print('\n¡Ok! Vamos a registrate en el sistema:\n')

        nombre = input('¿Cual es tu nombre?: ')
        apellido = input('¿Cual es tu apellido?: ')
        email = input('Introduce tu email: ')
        password = input('Introduce tu contraseña: ')

        usuario = user.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print (f'\n¡Perfecto! {registro[1]}, te has registrado con el email: {registro[3]}')
        else:
            print('\nNo te has registrado correctamente :/')


    def logueo(self):

        print('\n¡Ok! Ingresa en el sistema:\n')

        try:
            email = input('Introduce tu email: ')
            password = input('Introduce tu contraseña: ')

            usuario = user.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f'\n¡Bienvenido/a {login[1]}, te has registrado hoy {login[5]}!')
                self.proximasAcciones(login)

        except Exception as e:
            print(f'\n\t##### {(type(e).__name__)} #####\n')
            print('¡Logueo incorrecto, vuelva a intentarlo!')


    def proximasAcciones(self, usuario):

        print("""

        Acciones y comandos disponibles: 

        - Crear nota: (Crear)
        - Mostrar nota: (Mostrar)
        - Eliminar nota: (Eliminar)
        - Salir: (Salir)

        """)

        accion = input('Que quieres hacer?: ')
        usa = notas.acciones.Acciones()

        if accion == 'Crear':
            usa.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'Mostrar':
            usa.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 'Eliminar':
            usa.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 'Salir':
            print(f'\n¡Hasta pronto, {usuario[1]}!')
            exit()
 

        

  

 



 
























