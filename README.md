# RUN it
```
cd open_nsfw
docker build . -t warbling_cornhounds
docker run --network=host -p 5000:5000 --volume=$(pwd):/workspace warbling_cornhounds python ./server.py
python notporn.py
```