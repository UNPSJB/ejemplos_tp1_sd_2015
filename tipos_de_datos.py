# encoding: utf-8

print type(1)
print type('a')
print type("a")
t = ('localhost', 7000)


print type( t )
print t[0]
print t[1]
try:
    t[0] = 'otrohost' # La tupla es inmutable
except TypeError, e:
    print "La tuplas son immutables: ", e
print "-" * 40
print "Iteración"
for i in t:
    print i
    
for n, i in enumerate(t):
    print n, i

l = [1, 2, 4, 5, "hola", True, [2, 3]]
print l
print type(l)
l[0] = "otro valor"
print l

c = set( ['a', 'b', 'c', 'a'] )
print c

print "Esta 'a' en c?", 'a' in c


a = {'a': 1, 'b': 4, 'c': {'e': 5}}
print a

for k, v in a.items():
    print "%s = %s" % (k, v)

