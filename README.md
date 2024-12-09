# fall3340-app

[Sprint Planning](https://docs.google.com/spreadsheets/d/1Hz4CpsZgNapBO1e3kCuBihgrCgaK8QUm1_SiWbC72BM/edit?usp=sharing), [Technical](https://docs.google.com/document/d/1nES1agJkptSMXrpC6NSjp0JjgR4-98Bw/edit?usp=sharing&ouid=104017763662039089977&rtpof=true&sd=true) and [Design](https://docs.google.com/document/d/1CE0OFN7hN-9xSveZoVv2XKhH0Nn95g6IaNZLZCo5D00/edit?usp=sharing) Documentation

## Setup Instructions

1) git clone https://github.com/jmorin42/fall3340-app.git

2) create virtual environment: python -m venv virt

3) activate environment: source virt/Scripts/activate

4) install django and mysql:

	- pip install django
	- pip install MySQL
	- pip install mysql-connector-python
	- pip install mysqlclient
	- pip install django-decouple (for .env file and safety)

 	** for macOS users ONLY:
   	- pip install pymysql

6) cd into project file: cd fall3340-app
   
   ** to access your local mysql server you will have to update
   the *settings.py* and *mydb.py* files to change the user and
   password if they're not the same as mine

7) Add and edit *.env* file: touch .env

   - copy and paste the provided secret key into .env (may have to use an IDE like PyCharm, Sublime Text, etc.)

   ** also don't forget to update the user/password or any other variable to be accurate to your local MySQL server credentials

9) create database in local mysql server (if you don't already have one created): python mydb.py

   ** if you get an error here you probably already have a database by that name

10) create superuser: python manage.py createsuperuser

   	** for macOS users ONLY:
   	- Go into *\_\_init\_\_.py* in the *todoapp* directory and add these lines into the code:
   	  
   	  import pymysql
   	  
	  pymysql.install_as_MySQLdb()

11) migrate files: python manage.py makemigrations

    followed by: python manage.py migrate

12) run server: python manage.py runserver

Access the admin interface at https://localhost:8000/admin
using the superuser credentials
