# Prymus Django

## Library Project

### Steps to install

```
# Create virtual envoronment (once is enoguh!)
python -m venv venv

# Activate virtual environment (every time we start working with this project)
source venv/bin/activate

# Install all dependencies (every time a lib/dependency is added)
pip install -r requirements.txt
```

### Run

Activate venv before running this command!

```
python manage.py runserver
```

And go to http://127.0.0.1:8000/ in your browser!

### Apply database migrations

Activate venv before running this command! 

```
python manage.py migrate
```

### Create SuperUser (admin)

Activate venv before running this command!

```
python manage.py createsuperuser
```

### Tips

Depending on system you may shorten the runserver command:

```
# windows
manage.py runserver

# linux 
./manage.py runserver
```

To list all available commands, run `manage.py` script without parameters:

```
manage.py
```