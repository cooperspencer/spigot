# Docker Minecraft Spigot
This Dockerfile always builds the latest version of spigot


## Quick Start
```sh
docker pull buddyspencer/spugit
```

```sh
docker run \
  --rm \
  --name mc \
  -e MEMORYSIZE='1G' \
  -v /path/to/volume:/data:rw \
  -p 25565:25565 \
-i buddyspencer/spugit:latest
```
```sh
docker attach mc
```

## Availability
This container will be available for AMD64 and ARM64