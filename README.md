# EmperorBot
Simple chat bot  
You can check the docker images here - **https://hub.docker.com/repository/docker/h0d0user/god_emperor**

## How to start

### Ansible way - in development
`ansible bots_ship -m ping -i inventories/hosts -k`

### Docker way - recommended
`docker pull h0d0user/god_emperor:1.0`  
`docker run -d --restart=always --name god_emperor -e API_TOKEN=YOURTOKEN h0d0user/god_emperor:1.0`