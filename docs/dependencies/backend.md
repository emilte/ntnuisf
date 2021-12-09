# Documentation of tools in backend

This file primarily contains:

- \<tool-name\>
  - link to source
  - short description
  - what do we use it for and how?
  - [configurations]
  - [tips n' tricks]

<br>
<br>

# Table of contents:

- [Django](#django)
  - [django-simple-history](#django-simple-history)
  - [django-debug-toolbar](#django-debug-toolbar)
  - [django-user-agents](#django-user-agents)
  - [drf_yasg](#drf_yasg)
  - [django_db_logger](#django_db_logger)
  - [django-rest-framework](#django-rest-framework)
- [Other](#other)

<hr>
<br>

## Django

Section for documenting Django specific tools/dependencies.

<br>

### django-simple-history

[django-simple-history](https://django-simple-history.readthedocs.io/en/latest/) stores Django model state on every create/update/delete. This tool enables us to track modifications on our models and revert back to previous versions of an instance for whatever reason.

<br>

### django-debug-toolbar

[django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) is a very useful tool for revealing more information about each request and response on the frontend side during development. We can inspect a whole bunch of different things such as SQL-queries performed, backend-configurations, HTTP-headers, templates, static-files etc.

#### [Configuration](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html):

We only enable debug-toolbar during development. We do this by only providing endpoints in `feide-kp/urls.py` when `DEBUG=True`.

<br>

### django-user-agents

[django-user-agents](https://pypi.org/project/django-user-agents/) provides a set of utilities to be used in views and templates. These methods allows easy identification of visitor’s browser, OS and device information, including whether the visitor uses a mobile phone, tablet or a touch capable device.

<br>

### drf_yasg

TODO

<br>

### django_db_logger

TODO

<br>

### django-rest-framework

TODO

<br>
<br>

## Other

Section dedicated to other tools/dependencies not related to Django.

...
