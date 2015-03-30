# pubnub-api-example
simple example using the pubnub api in python and javascript

This demo expects a private-keys.sh file with the following structure

```
export PUB_KEY=pub-c-ffffffff-ffff-ffff-ffff-ffffffffffff 
export SUB_KEY=sub-c-ffffffff-ffff-ffff-ffff-ffffffffffff
export SEC_KEY=sec-c-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Run the launch.sh script with a path to the private-keys.sh file.

`./launch.sh private-keys.sh`

The script will prompt you for which of the script to execute. publishers publish random characters to channel "a", subscibers listen to all messages and print the channel name, original message, and the frequency for each character to STDOUT.

```
$ ./launch.sh private-keys.sh
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
