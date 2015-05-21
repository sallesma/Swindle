#! /bin/bash

# Update package list and upgrade all packages
sudo apt-get update

# Install debug tools
sudo apt-get -y install curl

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

#Install python Github librairie
sudo pip install PyGithub


# Requirements for headless Selenium tests
sudo apt-get install -y xvfb firefox xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

#Install selenium
sudo pip install selenium

# Virtual display for the Selenium tests
if ! grep -q "DISPLAY=:99" /home/vagrant/.profile
then
    echo "export DISPLAY=:99" >> /home/vagrant/.profile
fi
