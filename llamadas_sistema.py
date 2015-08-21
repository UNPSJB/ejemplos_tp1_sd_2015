import os


pid = os.fork()

if pid == 0:
    print "Soy el hijo", os.getpid()
else:
    print "Soy el padre", os.getpid()