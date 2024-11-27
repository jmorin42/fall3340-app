# fall3340-app

[Sprint Planning](https://docs.google.com/spreadsheets/d/1Hz4CpsZgNapBO1e3kCuBihgrCgaK8QUm1_SiWbC72BM/edit?usp=sharing) and [Design Documentation](https://docs.google.com/document/d/1CE0OFN7hN-9xSveZoVv2XKhH0Nn95g6IaNZLZCo5D00/edit?usp=sharing)

## Setup Instructions

1) git clone https://github.com/jmorin42/fall3340-app.git

2) create virtual environment: python -m venv virt

3) activate environment: source virt/Scripts/activate

4) install django and mysql:

	- pip install django
	- pip install MySQL
	- pip install mysql-connector-python
	- pip install mysqlclient

5) cd into project file: cd fall3340-app
   
   ** to access your local mysql server you will have to update
   the *settings.py* and *mydb.py* files to change the user and
   password if they're not the same as mine

6) create database in local mysql server (if you don't already have one created): python mydb.py

   ** if you get an error here you probably already have a database by that name

7) create superuser: python manage.py createsuperuser

8) migrate files: python manage.py migrate

9) run server: python manage.py runserver

Access the admin interface at https://localhost:8000/admin
using the superuser credentials
