# Overview #

Demonstrate using tcpdump to watch traffic on the default Docker bridge interface.
    
# Demo #

In one shell, start a tcpdump capture session:

```
docker run --rm -it --net=host corfr/tcpdump -i docker0
```

In another shell generate some network traffic from a container, e.g. using the [aws-cli](../aws-cli/README.md):

```
aws ec2 describe-instances
```

Observe the captured tcpdump output.
