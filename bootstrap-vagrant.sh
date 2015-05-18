#! /bin/bash

# Update package list and upgrade all packages
sudo apt-get update


# Install git
sudo apt-get -y install git
sudo apt-get -y install tig

# Install python pip3
sudo apt-get -y install python-pip

# Install django package
sudo pip install django

# Install Django REST Framework
sudo pip install djangorestframework
sudo pip install markdown
sudo pip install django-filter

# Install sqlite3
sudo apt-get install sqlite3

# Install debug tools
sudo apt-get -y install curl