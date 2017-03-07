from __future__ import print_function
import frida
import sys


session = frida.attach("hi")
script = session.create_script("""
 var st = Memory.allocUtf8String("TESTMEPLZ!");
 var f = new NativeFunction(ptr("%s"), 'int', ['pointer']);
  
 f(st)

 """ % int(sys.argv[1], 16))

def on_message(message, data):
 	print(message)
script.on('message',on_message)
script.load()
sys.stdin.read()