#!/bin/bash
docker ps --format "{{.Image}} {{.Ports}}" | grep zookeeper | grep -o ":\d\{5\}-" | cut -b 2-6
