FROM ubuntu


#Config python
RUN apt-get update && apt-get install -y python python-dev python-pip
RUN pip install feedparser psycopg2-binary

#Shut up tzdata
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata


#Config postgres
RUN apt-get install -my postgresql-10 postgresql-contrib-10

USER postgres

RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker docker

RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/10/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/10/main/postgresql.conf


EXPOSE 5432
EXPOSE 5050

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

USER root
RUN mkdir -p /scripts
RUN mkdir -p /scripts/data
RUN chown -R postgres:postgres /scripts/

USER postgres
#Add parser script
COPY scripts/* /scripts/


#Close config problem hole
RUN mkdir -p /var/run/postgresql/10-main.pg_stat_tmp
RUN chown postgres:postgres /var/run/postgresql/10-main.pg_stat_tmp -R

#Start postgres service
#CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/10/main", "-c", "config_file=/etc/postgresql/10/main/postgresql.conf"]
WORKDIR "/scripts"
CMD ["bash","menu.sh"]
