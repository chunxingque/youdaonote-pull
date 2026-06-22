django-admin startproject mysite

 

Put your code in some directory outside of the document root, such as /home/mycode.



 

editing mysite/settings.py, 

ALLOWED_HOSTS = ['*']


TIME_ZONE = 'Asia/Shanghai' 



cd into  

python manage.py startapp polls

Edit the polls/models.py

https://docs.djangoproject.com/en/3.1/intro/tutorial02/#creating-models

 

create polls/templates/polls/index.html

 

INSTALLED_APPS = [

'polls.apps.PollsConfig',#名字来自polls/apps.py file里

 

python manage.py makemigrations&python manage.py migrate

 

urlpatterns  https://docs.djangoproject.com/en/3.1/intro/tutorial03/#namespacing-url-names

https://docs.djangoproject.com/en/3.1/intro/tutorial01/#write-your-first-view

Use generic views https://docs.djangoproject.com/en/3.1/intro/tutorial04/#amend-urlconf

 

view

https://docs.djangoproject.com/en/3.1/intro/tutorial03/#a-shortcut-get-object-or-404

Use generic views https://docs.djangoproject.com/en/3.1/intro/tutorial04/#amend-views



python manage.py createsuperuser

redstoneleo

redstone-cold@163.com

redstone19910512

 

https://docs.djangoproject.com/en/3.1/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin

admin.site.register([Question, Choice])



python manage.py makemigrations&python manage.py migrate&python manage.py runserver 0.0.0.0:8000

 

