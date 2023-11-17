# ToDoList

Simple app for managing your tasks.

## Features

+ Add, update, remove tasks
+ Add, update, remove tags
+ Managing completing tasks

## Instalation

Python3 and Django must be already installed

```python
git clone https://github.com/HlovaOleh/to-do-list
cd to_do_list
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration
You can configure the application with the following environment variables:

* SECRET_KEY: is a crucial component of your Django project's security. 
It is used for various cryptographic operations and should be kept confidential. 
Do not share it publicly or expose it in your version control system.
* DEBUG: setting controls whether your Django application is in debug mode. 
In debug mode, detailed error pages are shown, making it easier to identify and fix issues during development. 
However, it's crucial to set `DEBUG` to `False` in production to avoid exposing sensitive information.
