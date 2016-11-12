var HOST = 'localhost'; // 146.148.105.55
var PORT = 36215;
var PROTO_PATH = __dirname + '/factorial.proto';

var grpc = require('grpc');
var protoDescriptor = grpc.load(PROTO_PATH);

var client = new protoDescriptor.MathService(HOST + ':' + PORT, grpc.credentials.createInsecure());

var input = {
    n: 5
};

client.factorial(input, function (err, output) {
    if (err) {
        console.log('error: ', err);
    } else {
        console.log('output: ', output);
    }
});