CALL docker rm -f app nginx
CALL docker-compose build --no-cache
CALL docker-compose up

 
