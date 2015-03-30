from collections import defaultdict
import re
import json
import random
import time
import os
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

def random_text():
	out = []
	while random.random() > 0.01:
		out.append(random.choice("abcefghijklmnopqrstuvwxyz"))
	return "".join(out)

while True:
	time.sleep(10)
	pubnub.publish(
		channel="a",
		message= "python:" + random_text(),
	)
