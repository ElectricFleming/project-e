# project-e

## Get setup locally: 
Install 
 * [ ] pgadmin 
 * [ ] nodejs
 * [ ] python3.7

```
$ python3.7 -m venv ./env

$ pip install -r requirements/local.txt

$ createdb project-e -U postgres --password <password>

$ export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/project-e
```

$ python manage.py migrate

<<<<<<< HEAD:README.md
### for more help 
https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#setting-up-development-environment
=======
$ python manage.py runserver


- https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#setting-up-development-environment
>>>>>>> c5ec1b37b90b4997307e88c456757504b670b342:README.rst

:License: Apache Software License 2.0


## Running projcet
--------
Build using 
<<<<<<< HEAD:README.md
``` npm i 
    npm run dev 
```
=======
   ``npm i``
   
   ``npm run dev``

>>>>>>> c5ec1b37b90b4997307e88c456757504b670b342:README.rst

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy project_e

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.




