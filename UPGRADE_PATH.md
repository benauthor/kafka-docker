# Testing the upgrade path

Requires: docker-compose

```
# build docker images
docker-compose build

# start with the old state. 4x 0.8.2.1 brokers.
docker-compose scale zookeeper=1
docker-compose scale kafka8=4
# (verify cluster is healthy)

# start the upgrade.
docker-compose scale kafka8=2 kafka9-intermediate=2
# (verify cluster is healthy)

## finish the version upgrade
docker-compose stop kafka8
docker-compose scale kafka9-intermediate=4
# (verify cluster is healthy)

## update the setting and do second round of restart
docker-compose scale kafka9-intermediate=2 kafka9-final=2
# (verify cluster is healthy)

docker-compose stop kafka9-intermediate
docker-compose scale kafka9-final=4
# (verify cluster is healthy)
```
