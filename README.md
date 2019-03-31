# Introduction
This application is build for implementing Media APIs.

# Installation

* Clone the Repo:
```
    $ git clone "https://github.com/yash-m-agarwal/task4_media_apis"
```

* Create the virtual environment and actiavte

```
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
```
* Change directory into the folder named task4_media_apis

* Install all the project dependencies
```
    $ pip install -r requirements.txt
```
* Make the database migrations
```
    $ python manage.py migrate
```

* Run the Server
```
    $ python manage.py runserver
```
* The above steps starts the development server on localhost:8000. Go to `http://localhost:8000/` in your browser.

# Configuring MySQL database:
The following segment guides how to use Mysql database

#### Configuring MySQL with the project(Linux)
* Install mysql and setup
```
    $ sudo apt-get update
    $ sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
    $ sudo mysql_secure_installation
``` 

* Install the django mysql depedencies(First activate the virtual environment)
```
    $ pip install mysqlclient
```

* Configure MySQL database
```
IN settings.py
Give appropriate values to the USER and PASSWORD fields, supply the ones you used to setup the mysql installation
Leave the NAME field as it is. This field is the name of the Database to use.
```

* Create the database of the same name as in the NAME field above. Assuming you left the field as it is with the name 'APIsMedia' type the following in the terminal :
```
    $ sudo service mysql start
    $ mysql -h 127.0.0.1 -u :username -p
```
:username is the username you provided during the mysql setup. If left as default it will be 'root'. The above command will prompt for a password as well. Provide the password used during the mysql setup

* To create the database (named APIsMedia)
```
    > CREATE DATABASE APIsMedia;
    > SHOW DATABASES;
```

Using SHOW DATABASES Command your created database will appear in the list of databases

* To use this database, again migrate
```
    $ python manage.py migrate
```

* Run the Server
```
    $ python manage.py runserver
```

# APIs Implemented:

* Base Url: `http:localhost:8000`

* `/`
    * GET Request
    * It is the landing page of the application, It contains 3 buttons.
        * Upload Image links to `/image/new`. 
        * View All Images links to `/images`
        * Find by name `/image` links to a form, where user can enter a name and submits, then it searches for all images created by that user.
    * It also conatains a list of links, each of `/image/<pk>` which represents an image record. On clicking a link, it leads to the image with a particular :id, 

* `/images`
    * GET Request
    * Retrieves all the image objects from the data base.
    * Displays each image object's **title**, **description**, **image** and **creator** in form of card, along with a link which leads to `/image/<pk>`
    
* `/image/new`
    * GET Request
    * Displays a form to submit an image from the User. After submitting the data a POST request generated which is redirected to the same url
    
    * POST request
    * On successful submission of the data it is redirected to the `/image/<pk>`
    
* `/image/<pk>`
    * GET Request
    * Retrieves an image object from the database with :id = pk. Displays all the attributes related to the image.
    * Displays two buttons.
        * Update button which links to `/image/<pk>/update` to update the image.
        * Delete button which links to `/image/<pk>/delete` to delete the image.

* `/image/search_name`
    * GET Request
    * Displays a form to submit a **created_by** field from the user. After submitting the form a POST request is generated which is redirected to `/image/<username>`

* `/image/<username>`
    * GET Request
    * Displays all the images which are createdby the :username.

* `/image/<pk>/update`
    * GET Request
    * Generates a form, where the user can update the image by adding a new one. It generates a PUT request which is redirected to the `/image/<pk>`
    

* `/image/<pk>/delete`
    * DELETE Request
    * It deletes the image object with the :id = pk.

# Database Schema:

#### Image(Table)

* Name
* Description
* Image
* Created_By
