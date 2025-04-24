#!/bin/bash

# Allow Docker to use the X server
xhost +local:docker

docker build --tag my_pyplot_docker .

# Run the container
docker run -it --rm \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	my_pyplot_docker

# Optionally revoke access after
xhost -local:docker