## Flask ToDo App

Simple CRUD app using Python and MySQL.

![Screenshot of the app.](https://github.com/AhmedMattar21/flask-todo-app/blob/master/static/images/todo-app.png)

### Run it using Docker Compose
```
$ cd flask-todo-app
$ docker compose up
```
### Run it using Docker with an external database
```
$ docker run -e MYSQL_ROOT_PASSWORD=YOUR_DB_ROOT_PASSWORD \
                MYSQL_HOST=YOUR_DB_HOST_NAME_OR_IP_ADDRESS  \
                MYSQL_USER=YOUR_DB_USERNAME \
                MYSQL_DB=YOUR_DB_NAME \
                -p 5000:5000 m4tt4r/flask-todo-app
```

### Run it using Python
```
$ cd flask-todo-app
$ pip3 install -r requirements.txt
$ export MYSQL_ROOT_PASSWORD=YOUR_DB_ROOT_PASSWORD \
         MYSQL_HOST=YOUR_DB_HOST_NAME_OR_IP_ADDRESS  \
         MYSQL_USER=YOUR_DB_USERNAME \
         MYSQL_DB=YOUR_DB_NAME 
$ flask run
```

> Python version 3.10.6
