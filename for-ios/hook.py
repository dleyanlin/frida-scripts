import frida
import sys


def on_message(message, data):
    try:
        if message:
            print("[*] {0}".format(message["payload"]))
    except Exception as e:
        print(message)
        print(e)


def do_hook():

    # https://github.com/frida/frida-gum/blob/34b62d52f41de56ee19693fa430f391115246d8c/tests/gumjs/script-darwin.m#L68
    # https://github.com/frida/frida-gum/blob/34b62d52f41de56ee19693fa430f391115246d8c/bindings/gumjs/gumjs-objc.js

    # $methods: array containing native method names exposed by this object

    hook = """
    if(ObjC.available) {
        for(var className in ObjC.classes) {
            if (ObjC.classes.hasOwnProperty(className)) {
                if(className == "class") {
                    send("Found our target class : " + className);
                }
            }
        }
        var hook = ObjC.classes.class["- hookfunc:"];
        Interceptor.attach(hook.implementation, {
            onEnter: function(args) {
                var receiver = new ObjC.Object(args[0]);
                send("Target class : " + receiver);
                send("Target superclass : " + receiver.$superClass);
                var sel = ObjC.selectorAsString(args[1]);
                send("Hooked the target method : " + sel);
                var obj = ObjC.Object(args[2]);
                send("Argument : " + obj.toString());
            }
        });
    } else {
        console.log("Objective-C Runtime is not available!");
    }
    """

    return hook

if __name__ == '__main__':
    try:
        process = frida.get_device_manager.enumerate_devices()[-1].attach("abc")
        session = process.session
        #session = frida.attach("FridaPlayGround")
        script = session.create_script(do_hook())
        script.on('message', on_message)
        script.load()
        sys.stdin.read()
    except KeyboardInterrupt:
        sys.exit(0)