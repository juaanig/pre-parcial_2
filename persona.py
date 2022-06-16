'''
Ejercicio 3
3.1 Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Implementar los siguientes métodos:
- Un constructor, donde los datos pueden estar vacíos.
- ``mostrar()``: Muestra los datos de la persona.
- ``esMayorDeEdad()``: Devuelve un valor lógico indicando si es mayor de edad.
'''
#=============================================================================================
class Persona():
    def __init__(self,nombre,edad,dni):
        self.nombre=nombre 
        self.edad=edad
        self.dni=dni

    def mostrar(self):
        valores = 'Nombre: {}\nEdad: {}\ndni: {}'.format(self.nombre,self.edad,self.dni)
        print(valores)

    def esMayorDeEdad(self):
        adulto = True if self.edad >= 18 else False
        return adulto
#=============================================================================================

