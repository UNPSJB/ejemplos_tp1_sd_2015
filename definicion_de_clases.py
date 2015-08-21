class Animal(object):
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Animal.contador += 1
    def __str__(self):
        """
        El toString() de Java/C++/PHP
        """
        return "Soy un Animal y me llamo %s" % self.nombre
    
    @classmethod
    def contador_de_instancias(cls):
        return "Hasta ahora instanciamos %d %s" % (cls.contador, cls)

print Animal.contador_de_instancias()
a = Animal("Gato")
print Animal.contador_de_instancias()
print a.contador_de_instancias()
#for i in range(1, 100, 7):
#    a = Animal.gatoFactory()
#    print a

