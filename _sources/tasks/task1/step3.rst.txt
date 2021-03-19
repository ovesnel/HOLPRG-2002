Step 3: Setup Django Project
############################

The first thing we need to do is to create a new DJANGO project, in order to do so, we will start a container with Python 3 and install DJANGO library.

The following docker commands will allow you to start a container from **python:3-slim-buster** image and executing a **bash** prompt.
The `-v` and `-w` switches allow us to map the local folder into the container in the `/app` directory and set the default workspace to `/app`.

From Visual Studio Code's terminal execute the following command:

.. code-block:: bash

    docker run -it -u 1000 --rm -v $PWD:/app -w /app python:3-slim-buster bash


Once we have a bash prompt inside the container, let's install django using Python's package manager.
In order to accomplish this, we will first create a virtual environment and activate it.

.. code-block:: bash

    python -m venv .venv
    source .venv/bin/activate
    pip install django

The following is the expected output after executing the command.

.. code-block:: bash

    I have no name!@796136e1b951:/app$ python -m venv .venv
    I have no name!@796136e1b951:/app$ source .venv/bin/activate
    I have no name!@796136e1b951:/app# pip install django
    Collecting django
    Downloading Django-3.1.7-py3-none-any.whl (7.8 MB)
    |████████████████████████████████| 7.8 MB 3.8 MB/s 
    Collecting sqlparse>=0.2.2
    Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
    |████████████████████████████████| 42 kB 1.2 MB/s 
    Collecting pytz
    Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
    |████████████████████████████████| 510 kB 3.6 MB/s 
    Collecting asgiref<4,>=3.2.10
    Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
    Installing collected packages: sqlparse, pytz, asgiref, django
    Successfully installed asgiref-3.3.1 django-3.1.7 pytz-2021.1 sqlparse-0.4.1

After DJANGO has been installed lets create a DJANGO project called `netprog`

.. Note ::

    We have decided to call this DJANGO project ``netprog``, if you decide to change the name, keep note of the name since it will need to be changed in other places later.

.. code-block:: bash

    django-admin startproject netprog

We can now safely exit the container.

.. code-block:: bash

   root@5109156083d2:/app# exit


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
