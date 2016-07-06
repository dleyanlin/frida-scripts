/*
var keyboard = ObjC.classes.ChatViewController_iPad["- doShowKeyboard"];

Interceptor.attach(keyboard.implementation, {
  onEnter: function(args) {
    // args[0] is self
    // args[1] is selector (SEL "sendMessageWithText:")
    // args[2] holds the first function argument, an NSString
    var message = ObjC.Object(args[1]);
    console.log("\n[ChatViewController_iPad doShowKeyboard:@\"" + message + "\"]");
  }
});

*/

for(var className in ObjC.classes) {
    if (ObjC.classes.hasOwnProperty(className)) {
        if(className == "wbxUINoAccountSearchMeeting") {
            console.log("\nFound our target class : " + className);
        }
    }
}

var hook = ObjC.classes.wbxUINoAccountSearchMeeting["- _joinMeeting:"];

var instance = hook.getInstance();
console.log("\n Instanve value is : " + instance);  

Interceptor.attach(hook.implementation, {
            onEnter: function(args) {

                var receiver = new ObjC.Object(args[0]);
                console.log("\nTarget class : " + receiver);
                console.log("\nTarget superclass : " + receiver.$superClass);

                var sel = ObjC.selectorAsString(args[1]);
                console.log("\nHooked the target method : " + sel);

                var obj = ObjC.Object(args[2]);
                console.log("\nArgument : " + obj.toString());
            }
});
