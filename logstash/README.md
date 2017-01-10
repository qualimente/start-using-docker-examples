# Overview #

Demonstrate a very-basic container logstash set-up. 

# Demo #

1. In shell 1, do `docker-compose up`
2. In shell 2, send some generated data into logstash's tcp port with:

```
while `true`; do echo "$(date +'%Y-%m-%d %H:%M:%S') logging tcp data $RANDOM" | nc localhost 5000; sleep 1; done;
```

3. In shell 2, run a container that logs to stdout with:

```
# important - do *not* attach tty via -t
docker run --rm alpine echo "$(date +'%Y-%m-%d %H:%M:%S') logging container stdout data $RANDOM"
```
