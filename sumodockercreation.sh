#!/bin/bash
set -xe
REGISTRY_USERNAME=sriniatdocker
REGISTRY_PASSWORD=Docker@4850
SUMO_VERSION=`curl -sI https://collectors.sumologic.com/rest/download/deb/64 | awk -F_ '/filename=sumocollector/ {print $2}'`
DOCKER_REGISTRY="hub.docker.com"
LOCAL_IMAGE_NAME="sumologic-collector:nosources_${SUMO_VERSION}"
REGISTRY_IMAGE_NAME="${DOCKER_REGISTRY}/${LOCAL_IMAGE_NAME}"
if [ ${OPERATION} == show_versions ] ; then
 echo "Current sumologic version: $SUMO_VERSION"
 #echo "Images available on Docker Hub:"
 #curl -s -X GET -u ${REGISTRY_USERNAME}:${REGISTRY_PASSWORD} https://${DOCKER_REGISTRY} .
elif [ ${OPERATION} == "build_image" ] ; then
 docker build --tag ${LOCAL_IMAGE_NAME} .
 docker tag ${LOCAL_IMAGE_NAME} ${REGISTRY_IMAGE_NAME}
 docker login -u ${REGISTRY_USERNAME} -p ${REGISTRY_PASSWORD} ${DOCKER_REGISTRY}
 docker push ${REGISTRY_IMAGE_NAME}
 docker rmi ${LOCAL_IMAGE_NAME} ${REGISTRY_IMAGE_NAME}
fi
