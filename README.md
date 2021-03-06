Course: https://realpython.com/courses/django-portfolio-project/


## Commands
To start the server:
`python manage.py runserver`

To open the Django shell:
`python manage.py shell`

###Migrations: 

Migrate: `python manage.py migrate`

Every time there's a new or edited model. We need to run first:
`python manage.py makemigrations`

### Adding data to database

Open the Django shell:

`python manage.py shell`

Create instance of model and save:

```
# Example
from projects.models import Project

p1 = Project(title="test project", description="this is a test", technology="Django", image="testproject.png")
p1.save()
```

### Reading data from database

Open the Django shell:

`python manage.py shell`

Query data:

```
# Example
from projects.models import Project

results = Project.objects.all()
results[0].title
```

## Django Template Language

Print variables: `{{ variable }}`

Also: `{% code logic %}`

For loops must be closed with `{% endfor %}`

Explore further syntax on [the official website.](https://docs.djangoproject.com/en/3.1/ref/templates/language/)

## admin usages

Create super user with the following command:

`python manage.py createsuperuser`

Access `http://127.0.0.1:8000/admin/` and log in.

From the admin page you can administrate model objects. Add in `admin.py` the models you want to manage from the admin
page.

```
# This registers the Project model
from projects.models import Project

admin.site.register(Project)
```

