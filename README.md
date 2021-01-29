for runnig the app 
 ### 1: Install postgresql on your pc and create a database named "contactsdb"
 ### 2: Install python, django, djangorestframeworka and django-cors-headers
 ### 3: From ```contactsapi/settings.py``` update ```DATABASES``` section with your own databases info
 ### 4: From ```contactsapi/settings.py``` update ```CORS_ORIGIN_WHITELIST``` section with your frontend apps info
 ### 4: Start a terminal on the folder that you located contactsapi and run
    ```python manage.py makemigrations```
    ```python manage.py migrate --run-syncdb```
    ```python manage.py runserver <PORT> // an empty port for running the api```
    
  
  
  
   
