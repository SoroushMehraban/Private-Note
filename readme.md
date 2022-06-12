# Private Note - Cloud computing project

> **Instructor**: [Dr. S. A. Javadi](https://scholar.google.com/citations?user=Va7RTUsAAAAJ&hl=en)

> **Contributors**: Soroush Mehraban and Mohammadreza Shahrestani

> **Semester**: Spring 2022
## About
![homepage](doc/homepage.jpg)
It's a simple project inspired from [Privnote.com](https://privnote.com).
## Steps
- [x] Implementing the webserver using Django.
- [ ] Containerize the project by writing a Dockerfile 
- [ ] Deploy the project on kubernetes
## Postgresql setup
Pull the image from DockerHub:
```text
docker pull postgres:alpine
```
Run the container:
```text
docker run --name postgres-0 -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine
```
Go inside the container:
```text
docker exec -it postgres-0 bash
```
Go inside the postgres:
```text
psql -U postgres
```
Create database
```text
create database privnote;
```
Now you can migrate the project on the terminal:
```text
python manage.py makemigration
python manage.py migrate
```
