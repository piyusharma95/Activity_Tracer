# Activity Tracer

**Activity Tracer** is a web application written in Django. The application utilizes [Django authentication system](https://docs.djangoproject.com/en/3.0/topics/auth/default/) User model to build Member model on top of it while storing the member's activities in ActivityPeriod. The application provides a custom management command `populatedb` to populate the database with dummy activities for each member and an [API](http://127.0.0.1:8000/memberinfo/) to showcase the data in JSON format.

## Getting Started
Clone the Github repo and install all the requirements from [requirements](https://github.com/piyusharma95/Activity_Tracer/blob/master/requirements.txt) file. Please note that the application dependencies should be installed in Windows OS. Run the Django server and follow the below steps:
1. Create a superuser in order to access the Django admin panel.
2. Create dummy users and their corresponding members in Users and Members tables respectively.
3. Run the management command `python manage.py populatedb` to create dummy activities for each member.
4. Visit the [API](http://127.0.0.1:8000/memberinfo/) which describes a list of users & their corresponding periods of activity across multiple months.
