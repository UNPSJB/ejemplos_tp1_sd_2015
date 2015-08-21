# encoding: utf-8
"""

"""
archivo = open('pepe.txt', 'w')


for i in range(10):
    archivo.write("2 x %d = %d\n" % (i, 2*i))

archivo.close()

print "Terminé de escribir el archivo"

archivo = open('pepe.txt', 'r')
for linea in archivo:
    print linea
    

 

