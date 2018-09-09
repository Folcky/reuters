# Reuters scrapper

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

## Requirements

 - Docker version: 18.06.1-ce
 - HDD free space: XGB
 - Internet connection

## Project files

| File | Description |
| ------ | ------ |
| run.sh | Build docker compose file and start interactive mode |
| Dockerfile | Dockerfile for Ubuntu server with Postgres-10 & Python 2.7  |
| docker-compose.yml | docker compose file with our app  |
| scripts | directory with scripts to work with Reuters, Postgres, data  |
| scripts/create_schema.sql | sql file to create schema  |
| scripts/export_data.py | python file to export data to csv file |
| scripts/get_data.py | python file to scrape RSS data from Reuters http://feeds.reuters.com/reuters/topNews  |
| scripts/lib.py | python file to check PostgreSQL schema  |
| scripts/save_data.py | python file to load data to PostgreSQL  |
| scripts/crontask.sh | Schedule scrape and save to PostgreSQL  |
| scripts/menu.sh | Bash menu for user as Entry point  |

## Install & Run

Go to the directory with the project files. Let's imagine that we are in Ubuntu. Run in terminal
$ cd reuters

Build & and run our app with run.sh file
```sh
$ bash run.sh
```

## Interact with reuters app menu

After running we can see bash menu in terminal:
```sh
$
1) Run PostgreSQL
2) Stop PostgreSQL
3) Create schema
4) Get some data from Reuters
5) Save data to PostgreSQL
6) Export data to CSV
7) Cron hourly
7) Quit
Please enter your choice: 
```

Type for example "1" without quotes to start PostgreSQL server than wait for starting. 

> Please, note that points 3 and 5
> work only if you have started PostgreSQL

> Please, note that point 6
> works only if you have scraped data with points 4 & 5



# Web interface for PostgreSQL

Go to your browser:
http://localhost/browser/

Web interface default credentials are:
```
user: example@example.com
password: example
```
PostgreSQL server default credentials are:
```
host: dev
user: postgres
password: postgres
```

### Todos

 - Check reuters news is already in database
 - Get news ids from link http://feeds.reuters.com......-idUSKCN1LP07Q
 - Clean news summary to suppress html tags
 - Link running proccess with news to monitor successful scraping


License
----

For fun


