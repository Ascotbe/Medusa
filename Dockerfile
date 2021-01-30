FROM ascotbe/medusa:latest
MAINTAINER ascotbe
WORKDIR /Medusa/Vue 
RUN npm install
WORKDIR /Medusa
CMD ["chmod +x run.sh"]
CMD ["./run.sh"]