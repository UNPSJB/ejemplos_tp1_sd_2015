import sys
try:
    import Pyro4
except ImportError:
    print "Te falta instalar Pyro4"
    sys.exit()


class Remoto(object):
    def saludar(self, nombre):
        return "Hola %s" % nombre

def main():
    objeto = Remoto()
    Pyro4.Daemon.serveSimple(
            {
                objeto: "ejemplo.remoto"
            },
            ns = False)

if __name__ == "__main__":
    main()
