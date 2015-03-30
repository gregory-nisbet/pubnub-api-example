from collections import defaultdict
import re
import json
import os
import Pubnub as PB

PUB_KEY = os.environ["PUB_KEY"]
SUB_KEY = os.environ["SUB_KEY"]
SEC_KEY = os.environ["SEC_KEY"]
CHANNEL_NAME = os.environ["CHANNEL_NAME"]

def frequency_count(text):
    "determine count of each letter"
    count = defaultdict(int)
    for char in text:
        count[char] += 1
    return count

def callback(message, channel):
    "print message, channel, and frequency count to STDOUT"
    print("python recevied:" + str({
        "channel": channel,
        "message": message,
        "frequency count":dict(frequency_count(message)),
    }))
    
def error(message):
    print({
        "error" : message
    })

if __name__ == "__main__":
    PB.Pubnub(
        publish_key = PUB_KEY,
        subscribe_key = SUB_KEY,
        secret_key = SEC_KEY,
        cipher_key = '',
        ssl_on = False,
    ).subscribe(
        channels=CHANNEL_NAME,
        callback=callback,
        error=error
    )
