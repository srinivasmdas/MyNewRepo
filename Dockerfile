
FROM ubuntu
ADD sumodockercreation.sh /root/myproject/MyNewRepo/sumodockercreation.sh
RUN chmod +x /root/myproject/MyNewRepo/sumodockercreation.sh
CMD ["/root/myproject/MyNewRepo/sumodockercreation.sh"]
RUN /usr/bin/docker build --tag ${LOCAL_IMAGE_NAME} .
RUN /usr/bin/docker tag ${LOCAL_IMAGE_NAME} ${REGISTRY_IMAGE_NAME}
RUN /usr/bin/docker login -u ${REGISTRY_USERNAME} -p ${REGISTRY_PASSWORD} ${DOCKER_REGISTRY}
RUN /usr/bin/docker push ${REGISTRY_IMAGE_NAME}
#RUN docker rmi ${LOCAL_IMAGE_NAME} ${REGISTRY_IMAGE_NAME}
