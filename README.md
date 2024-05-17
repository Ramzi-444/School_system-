
## Installation

Python and Django need to be installed

```bash
pip install django
```

## Usage
Connect Locally to database (Postgresql)     
Go to the School_system folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Login

The login page is common for students and teachers.  
The username is their name and password for everyone is 'project123'.  

Example usernames:  
student- 'Muzaffar'  
teacher- 'Nurlan'  

You can access the django admin page at **http://127.0.0.1:8000/admin** and login with username 'uca' and password '123'

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New students and teachers can be added through the admin page. A new user needs to be created for each. 

The admin page is used to modify all tables such as Students, Teachers, Departments, Courses, Classes etc.

## Deployed 

Visit the link and test the project which is already deployed https://school-system-nm7d.onrender.com  

The login page is common for admin, student and teacher:
Example usernames:  
student- 'Muzaffar' with password 'project123'  
teacher- 'Nurlan' with password 'project123'  
admin- 'uca' with password '123' 




