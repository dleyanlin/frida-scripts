'use strict';

//const co = require('co');
const async = require('generator-async');
const frida = require('frida');
//const load = require('frida-load');


let session, script;
async.run(function *() {
	const device = yield frida.getUsbDevice();
	const app = yield device.getFrontmostApplication();
	if (app === null )
		throw new Error("No app in foreground");
	session = yield device.attach(app.pid);
    script = yield session.createScript( '(' +
    	agent.toString() + ').call(this);');
    script.events.listen('message', message => {
    	console.log(message.payload.ui);
    	session.detach();
    });
    yield script.load();
});

function agent() {
	'use strict';

 ObjC.schedule(ObjC.mainQueue, () => {
    const window = ObjC.classes.UIWindow.keyWindow();
	const ui = window.recursiveDescription().toString();
	send({ui: ui});
});
}