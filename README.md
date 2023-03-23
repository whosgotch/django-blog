# Django-Blogger Website

Blogger website made with Django by @whosgotch

<p align="center">
   <img src="../main/blogger.png" alt="something went wrong...">
</p></br>

## Libraries and framework used
- Python
- Djano 4.2
- Bootstrap 4
- Pytest
- Factoryboy
- HTMX

## Functionality
- Post, update and create posts
- Edit markdown for posts online with Markdown library
- Read posts that another users posted

<p align="center">
   <img src="../main/single-post.png" alt="something went wrong...">
</p></br>


## Todo
- add tags functionality
- add search functionality

## How to run Django-Blogger on your computer

- Installation of the required files 
- Creating virtual environment
- Running Django Blogger on local host

### step 1
1 - Download [Python 3.9+](https://www.python.org/) and install it.

**OR**

Install using *scoop*.
```
> scoop install python
```

2 - Check Python version
```
> python --version

```

3 - Install virtualenv with pip install
```
> pip install virtualenv
```

### step 2
1 - Create virtual environment using virtualenv
```
> python -m virtualenv venv
```

2 - Activate virtual environment
```
> venv/scripts/activate
```

3 - Install Django using pip install
```

```

### step 3 
1 - Make a git clone of Django Blogger to your project folder
```
(venv) > git clone https://github.com/whosgotch/Django-Blogger.git
```

2 - Open project folder and install frameworks and libraries
```
(venv) > cd Django-Blogger
(venv) > pip install -r requirements.txt
```


3 - Run server, copy 127.0.0.1:8000 and paste it into your browser search bar.
```
(venv) > python manage.py runserver
```
