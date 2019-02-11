# milmove-admin
Test of Django admin for milmove project.

### Steps to run

##### In milmove project:

1. `make db_dev_e2e_populate`

##### In this project:

1. If you don't already have python 3.x, then `brew install python`
2. If you don't already have virtualenv, then `pip3 install virtualenv`
3. In the top level of this cloned repo, create a virtual environment: `virtualenv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install the requirements: `pip3 install -r requirements.txt`
6. Go into `milmove` folder and run `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the Django app: `python manage.py runserver`
9. Go to the admin in your browser and login with your superuser: `http://127.0.0.1:8000/admin`
10. Click on the `Moves` link to see a simple example of a Django admin (with some minimal
customization).  Other tables are currently just showing the default admin.
