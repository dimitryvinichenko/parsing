▎Python script that downloads news from the OKX crypto exchange

Project has the following structure:

- Dockerfile: File to build docker image.
- main.py: Parse arguments and run script.
- main.sh: Shell script to run application. Here we specify date range and name folder to store data.
- parser.py: Python script that downloads news from the OKX crypto exchange.
- requirements.txt: Libraries and their versions.

There are two ways to run the application. The first one is through creating a virtual environment and activating it. Then, in main.sh file, name the folder to store data and specify the date range, and finally run:
```bash
source main.sh
```

This will work on a local computer with an installed Chrome web browser.

The second way is better for a remote server. First, we need Docker to be installed on the remote server. This should help to install:

```bash
sudo apt-get update
sudo apt install docker.io
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

Then, we go to the directory with our project, tune variables in the main.sh file as we wish, and run:
```bash
docker build -t scraping .
docker run -ti scraping /bin/bash
```

Then, in the internal container terminal, we run:

```bash
source main.sh
```

And finally, upload data from the Docker container to the host:
```bash
docker cp <container id>:/app/data/ .
```
 
