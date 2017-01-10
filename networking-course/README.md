# Overview #

Demonstrate using a container for parts of the Udacity Networking for Web Developers course.

# Demo #

Start the [skuenzli/udacity-networking:2017-01-01](https://hub.docker.com/r/skuenzli/udacity-networking/) in a shell:

```
docker run -h networking-course --rm -it --name udacity_networking skuenzli/udacity-networking:2017-01-01
```

Perform some of the exercises.

## Interact with Udacity's webserver

```
printf 'HEAD / HTTP/1.1\r\nHost: www.udacity.com\r\n\r\n' | nc www.udacity.com 80
```

## Listen to a DNS request

```
tcpdump -i eth0
```

start another shell and enter container:

```
docker exec -it $(docker ps --quiet --filter name=udacity_networking) /bin/bash
```

issue a DNS request and observe tcpdump's captured output in other shell

```
dig www.google.com
```
