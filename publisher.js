var PB = require('pubnub');

var PUB_KEY = process.env.PUB_KEY; 
var SUB_KEY = process.env.SUB_KEY;
var SEC_KEY = process.env.SEC_KEY;
var CHANNEL_NAME = process.env.CHANNEL_NAME;

var pubnub = PB({
    publish_key : PUB_KEY,
    subscribe_key : SUB_KEY,
    secret_key : SEC_KEY,
});

var choice = function (arr) {
    return arr[Math.floor(arr.length * Math.random())];
}

var random_text = function () {
    out = []
    while (Math.random() > 0.03) {
        out.push(choice("abcdefghijklmnopqrstuvwxyz"));
    }
    return out.join();
};

var next = function () {
    pubnub.publish({
        channel : CHANNEL_NAME,
        message : random_text()
    });
}

setInterval(next, 500);
