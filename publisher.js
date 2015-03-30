var PB = require('pubnub');

pub_key = process.env.PUB_KEY; 
sub_key = process.env.SUB_KEY;
sec_key = process.env.SEC_KEY;

var pubnub = PB({
	publish_key : pub_key,
	subscribe_key : sub_key,
	secret_key : sec_key,
});

var choice = function (arr) {
	return arr[Math.floor(arr.length * Math.random())];
}

var random_text = function () {
	out = []
	while (Math.random() > 0.01) {
		out.push(choice("abcdefghijklmnopqrstuvwxyz"));
	}
	return out;
};

var next = function () {
	pubnub.publish({
		channel : "a",
		message : "node: " + random_text()
	});
}

setInterval(next, 5000);
