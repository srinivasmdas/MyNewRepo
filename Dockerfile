
FROM ubuntu
ADD sumodockercreation.sh ~/myproject/MyNewRepo/sumodockercreation.sh
RUN chmod +x ~/myproject/MyNewRepo/sumodockercreation.sh
CMD ["/myproject/MyNewRepo/sumodockercreation.sh"]
RUN docker build --tag ${LOCAL_IMAGE_NAME} .
RUN docker tag ${LOCAL_IMAGE_NAME} ${REGISTRY_IMAGE_NAME}
RUN docker login -u ${REGISTRY_USERNAME} -p ${REGISTRY_PASSWORD} ${DOCKER_REGISTRY}
RUN docker push ${REGISTRY_IMAGE_NAME}
RUN docker rmi ${LOCAL_IMAGE_NAME} ${REGISTRY_IMAGE_NAME}
