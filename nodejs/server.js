var config = require('./config');

var grpc = require('grpc');
var protoDescriptor = grpc.load(config.protoPath);
var client = new protoDescriptor.MathService(config.host + ':' + config.port, grpc.credentials.createInsecure());

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
    server.bind('0.0.0.0:' + config.port, grpc.ServerCredentials.createInsecure());
    console.log('Server started');
    server.start();
}

function getFactorial(call, callback) {
    var input = call.request.n;
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
