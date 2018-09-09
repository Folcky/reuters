#Build app
docker-compose up -d --build
#Run interactive mode
docker exec -ti reuters_dev bash menu.sh
