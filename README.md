# pubnub-api-example
This project is a simple example using the pubnub api in Python and JavaScript.
Publishers send a random sequence of characters (the exact length varies but is typically about 100) to a channel. Subscribes will watch for messages and give a frequency count. (Future versions may implement a Chi-Squared Test so you can see if your random number generator is any good.)

This demo expects a private-keys.sh file with the following structure

```
export PUB_KEY=pub-c-ffffffff-ffff-ffff-ffff-ffffffffffff 
export SUB_KEY=sub-c-ffffffff-ffff-ffff-ffff-ffffffffffff
export SEC_KEY=sec-c-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Run the run-example.sh script with a path to the private-keys.sh file.

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
python recevied:{'frequency count': {'l': 1, ' ': 1, 'n': 1, 'e': 1, 'd': 1, ':': 1, ',': 1, 'r': 1, 'o': 1}, 'channel': 'a', 'message': 'node: r,l'}
{"message":"node: r,l","channel":[["node: r,l"],"14276784485716672"],"frequency_count":{"n":1,"o":1,"d":1,"e":1,":":1," ":1,"r":1,",":1,"l":1}}
```
