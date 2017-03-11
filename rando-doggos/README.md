# Overview #

Simple demonstration of isolation features provided by Docker containers that allow you to explore software and try new things in a low-risk way.

# Demo - Build and Run a Simple Python Webapp #

This demo will show you how to build and run a simple Python webapp that displays a random cute dog!

## Build the image ##

```
docker image build -t rando-doggos . 
```

## Run the application ##

```
docker container run --rm -it -p 8888:5000 --name rando-doggos rando-doggos
```

## See cute dogs ##

Navigate to [http://localhost:8888 ](http://localhost:8888 ) in a web browser

