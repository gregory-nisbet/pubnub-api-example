var PB = require('pubnub');

var PUB_KEY = process.env.PUB_KEY;
var SUB_KEY = process.env.SUB_KEY;
var SEC_KEY = process.env.SEC_KEY;

var pubnub = PB({
    publish_key : PUB_KEY,
    subscribe_key : SUB_KEY,
    secret_key : SEC_KEY,
    cipher_key : '',
    ssl_on : false,
});

var frequency_count = function (text) {
    var i, count;
    count = {};
    for (i = 0; i < text.length; i++) {
        count[text[i]] = (count[text[i]] || 0) + 1;
    }
    return count;
};

pubnub.subscribe({
    channel: "a",
    callback: function (message, channel) {
        var out = {};
        out.message = message;
        out.channel = channel;
        out.frequency_count = frequency_count(message);
        console.log(JSON.stringify(out));	
    },
    error: function (message) {
        console.log( "node received: " +  JSON.stringify({"error" : message}) );
    }
});
