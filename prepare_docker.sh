# don't execute this file, source it: `source prepare_docker.sh`

# in the current docker-on-osx regime, you have to type these magic invocations
# every time you want to use docker. yawn.
docker_machine_name=default

docker-machine start $docker_machine_name
eval $(docker-machine env $docker_machine_name)
export DOCKER_IP=`docker-machine ip $docker_machine_name`

echo "Hey, your docker machine $docker_machine_name is running on $DOCKER_IP"
