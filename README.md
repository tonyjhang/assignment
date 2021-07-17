# Assignment

This project is integrate flask+uwgsi, mysql and nginx by using docker-compose.

## Logic
```
client --> nginx --proxy_pass(internal network)--> uwsgi server(flask) <----internal network  ----> mysql
```

## File structure
```
├── app
│   ├── apis
│   │   ├── __init__.py  # route logic
│   │   └── task.py  #task api logic
│   ├── config  # save necessary logic
│   └── models  # save database model
│   ├── app.py  #  configure flask and register blueprint
├── mysql  # init script for default user
├── nginx  # config proxy_pass between client and flask container
├── test  #  unittest login
└── wsgi.ini  #  config for uwsgi
```

## For developer
Install python depedency(remember to use virtualenv is better)
```sh
pip install -r requirements.txt
```

Pull mysql docker image
```sh
docker pull mysql/mysql-server:8.0.23
```
Run mysql container
```sh
docker run --name mysql -e MYSQL_ROOT_PASSWORD=changeme mysql/mysql-server:8.0.23
```
Configure db settings in app/config/db.py, then migrate it
```sh
python migrate.py
```
Run unit test(It will show some warning message in flask 1.1, it won't show after flask2)
```sh
pytest -v
```
## Run Demo
Build image
```sh
docker-compose build --no-cache
```
Run docker-compose
```sh
docker-compose up
```
Then the api can be seen in http://127.0.0.1:8001/tasks

Stop docker-compose
```sh
docker-compose stop
```
Remove related container
```sh
docker-compose rm -f
```
