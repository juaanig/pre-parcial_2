from persona import Persona
'''
### 3.2 Crear una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (es dinero asi que puede tener decimales). El titular será obligatorio y la cantidad es opcional. Implementar los siguientes métodos para la clase:
- Un constructor donde el titular es obligatorio y la cantidad opcional(0 por defecto)
- ``mostrar()``: Muestra los datos de la cuenta.
- ``ingresar(cantidad)``: se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
- ``retirar(cantidad)``: se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

'''

class Cuenta(Persona):

    def __init__(self,nombre,edad,dni,cantidad = 0):
        # Invoca al constructor de clase Persona
        super().__init__(nombre, edad, dni)
        self.cantidad = cantidad

    def ingresar(self,newCant):
        self.cantidad = 0 if newCant < 0 else self.cantidad + newCant
    

    def retirar(self,retiro):
        if retiro > self.cantidad:
            aviso = 'No posee saldo suficiente '
        else:
            aviso = 'Recuerde que tiene 30 segundos para retirar el dinero'
        return aviso

    def mostrar(self):
        super().mostrar()

try:
    cuenta1 = Cuenta('juan',22,41848143,2200000)
    cuenta1.mostrar()
    cuenta1.esMayorDeEdad()
    cuenta1.cantidad
    cuenta1.ingresar(100000)
    cuenta1.cantidad
    cuenta1.retirar(2400000)

except TypeError:
    print(TypeError)