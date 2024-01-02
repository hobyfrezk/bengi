# Bengi

# Local Setup

create and activate virtual enviornment

```bash
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

run local server
```bash
python app/manage.py runserver
python app/manage.py tailwind start

"""
handy command
"""
# create new app
cd app
python manage.py startapp appname

# migrate db
python app/manage.py makemigrations
python app/manage.py migrate

# create super user
python app/manage.py createsuperuser

# enter shell
python app/manage.py shell

```