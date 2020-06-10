FROM  ascotbe/medusa:0.84
RUN cd /Medusa/ \
    && chmod 755 /Medusa/start.sh

CMD ["./Medusa/start.sh"]
