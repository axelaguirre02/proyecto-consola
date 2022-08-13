# ¡Proyecto de consola con Python y MySQL!

from usuarios import acciones

print("""

Acciones disponibles:

   - Registrarme
   - Loguearme

""")

hazEl = acciones.Acciones()

accion = input('¿Que quieres hacer?: ')

if accion == 'Registrarme':
    hazEl.registro()


elif accion == 'Loguearme':
    hazEl.logueo()












 


















