FROM nginx:1.16-alpine
RUN  apk -U upgrade && apk add nano && apk add vim && apk add bash  && apk add curl && apk add htop
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]