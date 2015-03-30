trap "kill -TERM -- -$$" EXIT

function fatal_error {
    echo "ERROR: $1"
    exit 1
}

if [ $# -ne 1 ]; then
    fatal_error "wrong number of arguments! expects 1"
fi

if [ ! -f "$1" ]; then
    fatal_error "file $1 does not exist!"
fi

source "$1"

[[ ! -z "$PUB_KEY" ]] || fatal_error "no publisher key"
[[ ! -z "$SUB_KEY" ]] || fatal_error "no subscriber key"
[[ ! -z "$SEC_KEY" ]] || fatal_error "no secret key"
[[ ! -z "$CHANNEL_NAME" ]] || CHANNEL_NAME="chars"
export CHANNEL_NAME

function prompt {
    local question=$1
    local cmd=$2

    local no_response_yet=1
    while [ $no_response_yet -eq 1 ]
    do
        read -p "$question" response
        case "$response" in
            [Yy]* ) 
                no_response_yet=0; $cmd & ;;
            [Nn]* ) 
                no_response_yet=0 ;;
            * ) 
                echo "'yes' or 'no' please" ;;
        esac
    done
}

prompt "launch python publisher  (y/n)? " "python publisher.py"
prompt "launch nodejs publisher  (y/n)? " "node publisher.js"
prompt "launch python subscriber (y/n)? " "python subscriber.py"
prompt "launch nodejs subscriber (y/n)? " "node subscriber.js"

sleep 9999
