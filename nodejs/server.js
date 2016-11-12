var HOST = 'localhost'; // 146.148.105.55
var PORT = 36215;
var PROTO_PATH = __dirname + '/factorial.proto';

var grpc = require('grpc');
var protoDescriptor = grpc.load(PROTO_PATH);
var client = new protoDescriptor.MathService(HOST + ':' + PORT, grpc.credentials.createInsecure());

function getServer() {
    var server = new grpc.Server();
    server.addProtoService(protoDescriptor.MathService.service, {
        factorial: getFactorial
    });
    return server;
}

if (require.main === module) {
    // If this is run as a script, start a server on an unused port
    var server = getServer();
    server.bind('0.0.0.0:36215', grpc.ServerCredentials.createInsecure());
    server.start();
}

function getFactorial(call, callback) {
    var input = call.request.n;
    console.log('got', input);
    if (input === 1) {
        callback(null, {result: 1});
    } else {
        client.factorial({n: input - 1}, function (err, output) {
            if (err) {
                console.log('error: ', err);
            } else {
                callback(null, {result: input * output.result})
            }
        });

    }
}
