## Iprorate
This is python script that is used to request new ip to the tor. Through this you can change your ip adderes which you can use this
module while brute forcing.

### Tor

This module use tor to change Ip address. To install tor, run the below command.

`sudo apt-get install tor`

### Python libraries

* requests
* requests[socks]
* stem

## Documentation

### Class initialization

IProtator class takes five positional arguments and tow optional keyword arguments.

#### url

> It's a tuple of url and data

#### method  

> String datatype that specify the http method

#### thread_lmt

> Integer datatye that specify the max. no. of threads

#### response_handler

> function object that handles the response returned from the server

#### sleep_time

> Integer datatype that provide to sleep time between two Ip changes.

#### headers

> It's a dictionary datatype. Which provides the headers to the request. It's an optional parameter.

#### rotateIP

> It's a boolean datatype. It's controll the IP rotation.
> It's an optional argument. By default it's True.

### Tor Config

> To use this script first we need to configure the tor properly

    VirtualAddrNetwork 10.192.0.0/10
    AutomapHostsOnResolve 1
    TransPort 9040
    SocksPort 9050
    ControlPort 9051
    DNSPort 53
    RunAsDaemon 1
    CookieAuthentication 0

copy the above configuration and paste it in /etc/tor/torrc
