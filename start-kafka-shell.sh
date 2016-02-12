#!/bin/bash
zk_port=`./zk_port.sh`
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -e HOST_IP=$DOCKER_IP -e ZK=$DOCKER_IP:$zk_port -i -t wurstmeister/kafka /bin/bash
