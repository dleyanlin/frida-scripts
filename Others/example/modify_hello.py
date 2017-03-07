import frida
import sys


session = frida.attach("hello")
script = session.create_script("""
Interceptor.attach(ptr("%s"), {
     onEnter: function(args) {
         args[0] = ptr("1111");
         args[1] = ptr("1111");
     }
 });
 """ % int(sys.argv[1], 16))

script.load()
sys.stdin.read()