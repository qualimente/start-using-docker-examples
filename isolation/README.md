# Overview #

Simple demonstration of isolation features provided by Docker containers that allow you to explore software and try new things in a low-risk way.

# Demo - Filesystem Isolation #

Start a fresh container:

```
# important note: notice there are no volumes mounted with -v 
# which would mount external data into the container and make it susceptible to destruction 
yourhost$ docker run -h isolation --rm -it centos:7.2.1511 bash
```

Double-check you are inside the container, about to destroy the filesystem!  Your shell prompt should look like:

```
[root@isolation /]#
```

Now...on with the destruction!

```
# list files in /usr/bin to prove this is a normal CentOS installation
[root@isolation /]# ls /usr/bin

# remove all files in /usr/bin!
[root@isolation /]# rm -rf /usr/bin

# try listing files again
[root@isolation /]# ls /usr/bin
```

The second listing of `/usr/bin` should result in an error: `bash: ls: command not found` because the `ls` program has been removed.

Type `exit` to leave the broken container.

Now to prove nothing on the host has been affected start a new container and list `/usr/bin` again:

```
yourhost$ docker run -h isolation --rm -it centos:7.2.1511 bash
```

```
[root@isolation /]# ls /usr/bin
```