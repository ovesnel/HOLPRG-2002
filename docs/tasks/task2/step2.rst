Step 2: Create a Django Application
###################################

The first thing that needs to be done is to create an application for us to capture the interfaces.
Each application you write in Django consists of a Python package that follows a certain convention.
In our case we will call this application **interfaces**.

To create it, let's open another terminal (**without closing the one where docker-compose is running**) and execute a shell into the exsiting container:

.. code-block::

    [cisco@centos HOLPRG-2002]$ docker exec -it cl_app_1 bash
    root@5109156083d2:/app# 

Once in the application's bash shell, let's create the Django application by issuing the following command:

.. code-block::

    ./manage.py startapp interfaces

This will create the directory :guilabel:`netprog/interfaces` in our host machine, which is mapped to the :guilabel:`/app/interfaces` directory within the container.
It will have the following Django structure:

.. code-block::

    root@5109156083d2:/app# ls -la interfaces/
    total 24
    drwxr-xr-x. 3 root root 4096 Mar 17 21:12 .
    drwxr-xr-x. 4 root root   70 Mar 17 21:12 ..
    -rw-r--r--. 1 root root    0 Mar 17 21:12 __init__.py
    -rw-r--r--. 1 root root   63 Mar 17 21:12 admin.py
    -rw-r--r--. 1 root root   95 Mar 17 21:12 apps.py
    drwxr-xr-x. 2 root root   24 Mar 17 21:12 migrations
    -rw-r--r--. 1 root root   57 Mar 17 21:12 models.py
    -rw-r--r--. 1 root root   60 Mar 17 21:12 tests.py
    -rw-r--r--. 1 root root   63 Mar 17 21:12 views.py


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
