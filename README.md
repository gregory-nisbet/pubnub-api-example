# pubnub-api-example
This project is a simple example using the pubnub api in Python and JavaScript.
Publishers send a random sequence of characters (the exact length varies but is typically about 100) to a channel. Subscribes will watch for messages and give a frequency count. (Future versions may implement a Chi-Squared Test so you can see if your random number generator is any good.)

This demo expects a private-keys.conf file with the following structure

```
export PUB_KEY=pub-c-ffffffff-ffff-ffff-ffff-ffffffffffff 
export SUB_KEY=sub-c-ffffffff-ffff-ffff-ffff-ffffffffffff
export SEC_KEY=sec-c-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Run the run-example.sh script with a path to the private-keys.conf file.

`./run_examples.sh private-keys.conf`

The script will prompt you for which of the script to execute. Publishers publish random characters to channel set by the environment variable CHANNEL_NAME or "chars" if none is set. Subscibers listen to all messages and print the channel name, original message, and the frequency for each character to STDOUT.

```
$ ./run_examples.sh private-keys.conf
launch python publisher  (y/n)? y
launch nodejs publisher  (y/n)? y
launch python subscriber (y/n)? y
launch nodejs subscriber (y/n)? y
```

example output:

```
python recevied:{'channel': 'chars', 'message': 'dtzhnavilexlbloxvjhletnpcamnifhlapudnhmvzbjfaizicspkdhvtgxmxvysoqftsvgslgvxmfkqsbqsocslkagyjwcuslgftzkzewilhcnjltawquxxtmdgbumtpvdmcxeoquhuetuyomoyfmeqtfbaodsxclcfgvrfpulisqdydytjvatpldwtzzmmhugmcbc', 'frequency count': {'u': 9, 'n': 5, 'l': 13, 't': 13, 'z': 7, 'x': 9, 'd': 9, 'y': 6, 'm': 12, 'g': 8, 'i': 6, 'v': 10, 'q': 7, 'j': 5, 'o': 7, 'e': 6, 'p': 6, 'r': 1, 'w': 4, 'b': 6, 's': 10, 'a': 8, 'f': 9, 'h': 8, 'c': 10, 'k': 4}}
```
