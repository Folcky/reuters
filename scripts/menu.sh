#!/bin/bash


PS3='Please enter your choice: '
options=("Run PostgreSQL" "Stop PostgreSQL" "Create schema" "Get some data from Reuters" "Save data to PostgreSQL" "Export data to CSV" "Cron hourly" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Run PostgreSQL")
            #/usr/lib/postgresql/10/bin/postgres -D /var/lib/postgresql/10/main -c config_file=/etc/postgresql/10/main/postgresql.conf &
            /etc/init.d/postgresql start
            psql --command "ALTER USER postgres WITH PASSWORD '$POSTGRES_PASSWORD';"
            ;;
        "Stop PostgreSQL")
            /etc/init.d/postgresql stop
            ;;
        "Create schema")
            psql -a -f create_schema.sql
            ;;
        "Get some data from Reuters")
            python get_data.py
            ;;
        "Save data to PostgreSQL")
            python save_data.py
            ;;
	"Export data to CSV")
            python export_data.py
            ;;
        "Cron hourly")
            bash crontask.sh
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
