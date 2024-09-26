docker run -it -p 8080:8080 -v /workspace/excercice_docker/Docker02/webapp/static/pdf:/home/webapp/static/pdf volumenes:1

docker run -it -p 8080:8080 v:1


docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker rmi $(docker images -a -q)