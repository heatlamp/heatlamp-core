# Heatlamp Core

*Keep your Docker images fresh*

Heatlamp enables simple continuous deployment for Docker images. It accepts a webhook POST from DockerHub (or somewhere else) whenever a new image has been created and performs some action in response, presumably one that will pull the new image and relaunch any containers that are now outdated.

Although you *can* use the `heatlamp/core` image directly, you'll most likely want to use a child image that customizes it for a specific configuration management tool. Look around this organization to see if there's one that already meets your needs.

## Use

Launch heatlamp/core with `docker`. You'll need to mount the Docker socket so that heatlamp will be able to perform Docker actions on your behalf, and to map the heatlamp port so the webhook can be accepted. Configure the settings listed below by customizing the container's environment.

```bash
docker run heatlamp/core \
  --volume /var/run/docker.sock:/var/run/docker.sock \
  --port 10100:10100 \
  --restart always
```

## Configure

Configure Heatlamp by setting environment variables within the container.

*Pending*
