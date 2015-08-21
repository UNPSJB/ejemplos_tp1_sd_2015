import sys
try:
    import Pyro4
except ImportError:
    print "Te falta instalar Pyro4"
    sys.exit(-1)

objeto_remoto = Pyro4.Proxy("PYRO:ejemplo.remoto@localhost:56296")
print objeto_remoto.saludar("Juan")
