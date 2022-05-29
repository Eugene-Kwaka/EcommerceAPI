# EcommerceAPI
Django EcommerceAPI for books and products. Can be coupled with any Frontend framework of choice.

# Table of Contents
- [Background](#background)
- [Minimum Requirements](#minimum-requirements)
- [Quickstart](#quickstart)


## Background
This project is an EcommerceAPI built with Django Rest Framework to show a Cart containing Books and Products(Other than books). It applies CRUD(Create, Read, Update and Delete) functionality on the Books, Products and the Cart that holds the items. 
The project also applies JWT Authentication to register and login users. The API is written with Class-Based Views (CBV) with focus on core fundamentals which are easy to read, understand and implement.


## Minimum Requirements
This project supports Ubuntu Linux 20.04 and Windows OS with their previous stable releases. It has not been tested on Mac OS.

- [Python3](https://www.python.org/downloads/)
- [Django 4.0.4](https://www.djangoproject.com/)
- [Git](https://git-scm.com/downloads)


## Quickstart
```bash
$ mkdir djangoecommerceapi
$ cd djangoecommerceapi
$ git init
$ git clone https://github.com/Eugene-Kwaka/EcommerceAPI.git
$ cd EcommerceAPI
$ sudo apt install python3-pip python3-django
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```
