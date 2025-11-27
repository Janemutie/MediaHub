### MEDIA HUB
Media sharing platform thta has role based access
- teacher role - manage assigned student cintent,media uploads
- student role - share media uploads
- admin role - overseeing all content and managing the platform

## Tools for use
-django frameworks
-python libraries (ready made snippets for a specific job)
    - pillow : media transactions in python frameworks (absolute media url, )
    - cloudinary : media storage and also url acccess generation (url -> save to database for an upload)
    -python-decouple : media tasks

## Apps in projects
    -accounts : handle authentication and authorization (sign ups,login,forgot password)
    -media_assets : uploads tasks, displays , updates

## Steps
- install the libraries :
    pip install libraryname
    pip install -r requirements.txt 
- create our apps (accounts and media_assets)
- configure our project settings
    - register our apps
    - register cloudinary (give the claudinary configs)
    - register a custom authentication process
    - emails registry
    
### Authentication and Authentication
Authentication = identity identification, who are you
Authorization = access priviledges - role based authorization , token based authorization

1. Cretae our custom user models -> models.py
2. Extend the integrate form captures -> forms.py
3. Create the views action for registration and login,logout and profile view, custompasswordresetview,custompasswordrestconfirmresetview -> views.py
4. Register the view actions as URL route - urls.py
5. Register the models for admin to use and manage content on - admin.py
6. Register th apps url to project urls = project/urls.py
7. Create the templates
    - create a templates folder - within the app
    - create a global templates folder - register it's configuration in the settings.py file
8. Make a database migrations and then populate the templates
    python manage.py makemigrations
    python manage.py migrate

## Template Creation
1. Configuration level file : base.html
    - Defining your blocks : title, extra_css ,  content(most important), footer, extra_js
    - Linking to global stylesheet / style lib. (bootstrap)
    - link to global js files

2. Create the other pages by simply extending configs done on 1.
    Populate what is dynamic using block

## Model View Templates