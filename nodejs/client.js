var config = require('./config');
var grpc = require('grpc');
var protoDescriptor = grpc.load(config.protoPath);

var client = new protoDescriptor.MathService(config.host + ':' + config.port, grpc.credentials.createInsecure());

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