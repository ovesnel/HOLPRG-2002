Step 3: Setup Django Project
############################

The first thing we need to do is to create a new Django project, in order to do so, we will start a container with Python 3 and install Django library.

The following docker commands will allow you to start a container from **python:3-slim-buster** image and executing a ``bash`` prompt.
The `-v` and `-w` switches allow us to map the local folder into the container in the :guilabel:`/app` directory and set the default workspace to :guilabel:`/app`.

From Visual Studio Code's terminal execute the following command:

.. code-block:: bash

    docker run -it -u 1000 --rm -v $PWD:/app -w /app python:3-slim-buster bash

.. note::

    Do not be surprised if you get a prompt that says `I have no name!`.
    This is due to us using UID 1000 which belongs to your ``cisco`` user, but does not exist inside the container. 

Once we have a bash prompt inside the container, let's install django using Python's package manager.
To accomplish this, we will first create a virtual environment and activate it.

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

.. tip::

    You might receive a warning from VSCode similar to this one:

    .. image:: images/vscode-too-many-files-changed.png
        :width: 25%


    This is expected.
    Press the `x` to dismiss the warning.

After Django has been installed let's create a Django project called **netprog**:

.. Note ::

    We have decided to call this Django project **netprog**, if you decide to change the name, keep note of the name since it will need to be changed in other places later.

.. code-block:: bash

    django-admin startproject netprog

We can now safely exit the container, use the ``exit`` command to accomplish the task.

.. code-block:: bash

    exit

.. sectionauthor:: Ali Eftekhari <aleftekh@cisco.com>, Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>

