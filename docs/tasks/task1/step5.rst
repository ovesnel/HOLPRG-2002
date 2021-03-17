Step 5: Build and Run Our Application Container
###############################################


Now that our Dockerfile is ready, we will need to build and image using the Dockerfile, in order to do so execute the following command:

.. code-block:: bash

   docker build . -t holprg2002

Now that we have a container image with our application, lets run the container with our application with the following command:

.. code-block:: bash

   docker run -it --rm -p 80:80 -v $PWD/netprog:/app -w /app holprg2002

After executing the above command you will see the application start and the server will be listening in port 80.
To stop the application and thus stop the container, press ``^C``.

.. code-block::

   ❯ docker run -it --rm -p 80:80 -v $PWD/netprog:/app -w /app holprg2002
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).

   You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
   Run 'python manage.py migrate' to apply them.
   March 17, 2021 - 19:48:45
   Django version 3.1.7, using settings 'netprog.settings'
   Starting development server at http://0.0.0.0:80/
   Quit the server with CONTROL-C.

Open your browser and go to http://localhost and you should see the following page loaded:

.. image:: images/django-welcome-page.png
    :width: 75%
    :align: center

Lets now stop our server by pressing ``^C``


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
