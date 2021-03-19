Step 5: Build and Run Our Application Container
###############################################


Now that our Dockerfile is ready, we will need to build a Docker image using the Dockerfile, in order to do so execute the following command:

.. code-block:: bash

   docker build . -t holprg2002

The following is a sample output from the above command:

.. code-block::

   [cisco@centos HOLPRG-2002]$ docker build . -t holprg2002
   Sending build context to Docker daemon  71.68MB
   Step 1/7 : FROM python:3-slim-buster
   ---> b2b5367cdfd4
   Step 2/7 : WORKDIR /app
   ---> Using cache
   ---> 53b824823ab5
   Step 3/7 : COPY requirements.txt .
   ---> Using cache
   ---> c54c097d8d9c
   Step 4/7 : RUN pip install -r requirements.txt --no-cache-dir
   ---> Using cache
   ---> 4cd369b916dd
   Step 5/7 : COPY ./netprog .
   ---> daa96094c69e
   Step 6/7 : RUN chgrp -R 1000 /app &&    chmod -R g+rwX /app
   ---> Running in 4319cea0e80d
   Removing intermediate container 4319cea0e80d
   ---> a0db22be858c
   Step 7/7 : CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]s
   ---> Running in 6e747ac80f78
   Removing intermediate container 6e747ac80f78
   ---> 247a6e234903
   Successfully built 247a6e234903
   Successfully tagged holprg2002:latest

Now that we have a container image with our application, let's run the container with the following command:

.. code-block:: bash

   docker run -it -u 1000 --rm -p 80:8080 -v $PWD/netprog:/app -w /app holprg2002

After executing the above command you will see the application start and the server will be listening in port 80.

.. code-block::

   [cisco@centos HOLPRG-2002]$ docker run -it -u 1000 --rm -p 80:8080 -v $PWD/netprog:/app -w /app holprg2002
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).

   You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
   Run 'python manage.py migrate' to apply them.
   March 17, 2021 - 19:48:45
   Django version 3.1.7, using settings 'netprog.settings'
   Starting development server at http://0.0.0.0:8080/
   Quit the server with CONTROL-C.

Open your browser and go to http://localhost. You should see the following page loaded:

.. image:: images/django-welcome-page.png
    :width: 75%
    :align: center

Lets now stop our application and container by pressing ``^C``.


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
