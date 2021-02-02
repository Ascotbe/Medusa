FROM ascotbe/medusa:latest
MAINTAINER ascotbe
WORKDIR /Medusa
RUN git pull
WORKDIR /Medusa/Vue 
RUN npm install
WORKDIR /Medusa
CMD ["chmod +x run.sh"]
CMD ["./run.sh"]