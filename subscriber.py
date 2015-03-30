from collections import defaultdict
import re
import json

import Pubnub as PB

pub_key = os.environ["PUB_KEY"]
sub_key = os.environ["SUB_KEY"]
sec_key = os.environ["SEC_KEY"]

pubnub = PB.Pubnub(
	publish_key = pub_key,
	subscribe_key = sub_key,
	secret_key = sec_key,
	cipher_key = '',
	ssl_on = False,
)

def frequency_count(text):
	count = defaultdict(int)
	for char in text:
		count[char] += 1
	return count

def callback(message, channel):
	print("python recevied:" + str({
		"channel": channel,
		"message": message,
		"frequency count":dict(frequency_count(message)),
	}))
	
def error(message):
	print({
		"error" : message
	})

pubnub.subscribe(
	channels="a",
	callback=callback,
	error=error
)
