# Installing Docker Desktop

## Prerequisites

To install Docker Desktop successfully, you must:

Meet the system requirements

Have a 64-bit version of either Ubuntu Lunar Lobster 23.04 or Ubuntu Jammy Jellyfish 22.04 (LTS) Docker Desktop is
supported on x86_64 (or amd64) architecture.

For non-Gnome Desktop environments, gnome-terminal must be installed:

```shell
sudo apt install gnome-terminal
```

Uninstall the tech preview or beta version of Docker Desktop for Linux. Run:

```shell
sudo apt remove docker-desktop
```

For a complete cleanup, remove configuration and data files at $HOME/.docker/desktop, the symlink at
/usr/local/bin/com.docker.cli, and purge the remaining systemd service files.

Install using the Apt repository
Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository.
Afterward, you can install and update Docker from the repository.

Set up Docker's Apt repository.

# Add Docker's official GPG key:

```shell
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

# Add the repository to Apt sources:

```shell
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

# Install the Docker packages.

Latest Specific version

To install the latest version, run:

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify that the Docker Engine installation is successful by running the hello-world image.

```shell
docker run hello-world
```

-> Hello from Docker!

This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation
message and exits.

You have now successfully installed and started Docker Engine.

## docker-compose

```shell
docker-compose build
```

```shell
docker-compose up
```

```shell
docker-compose exec app python manage.py migrate
```
