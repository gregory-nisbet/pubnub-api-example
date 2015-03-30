from collections import defaultdict
import re
import json
import random
import time
import os
import Pubnub as PB

PUB_KEY = os.environ["PUB_KEY"]
SUB_KEY = os.environ["SUB_KEY"]
SEC_KEY = os.environ["SEC_KEY"]
CHANNEL_NAME = os.environ["CHANNEL_NAME"]

pubnub = PB.Pubnub(
    publish_key = PUB_KEY,
    subscribe_key = SUB_KEY,
    secret_key = SEC_KEY,
    cipher_key = '',
    ssl_on = False,
)

def random_text():
    "generate a random string with a random length"
    out = []
    while random.random() > 0.03:
        out.append(random.choice("abcefghijklmnopqrstuvwxyz"))
    return "".join(out)

if __name__ == "__main__":
    while True:
        pubnub.publish(
            channel=CHANNEL_NAME,
            message= "python:" + random_text(),
        )
        time.sleep(4)
