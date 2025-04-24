#!/bin/bash

# Allow Docker to use the X server
xhost +local:docker

docker build --tag my_pyplot_docker .

# Run the container
docker run -it --rm \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	my_pyplot_docker
# Run the Docker container with GUI support
docker run -it --rm \
	-e DISPLAY=$DISPLAY \					# Pass the DISPLAY environment variable so GUI apps know where to render
	-v /tmp/.X11-unix:/tmp/.X11-unix \		# Share the X11 Unix socket to allow GUI communication with the host
	my_pyplot_docker						# Replace with the name of your Docker image

# Optionally revoke access after
xhost -local:docker