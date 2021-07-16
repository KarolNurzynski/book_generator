echo "Removing old docker container if exists"
docker rm -f app nginx

echo "Build new docker"
docker-compose build --no-cache 

echo "running docker componse"
docker-compose up
 
