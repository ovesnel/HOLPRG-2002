Step 6: Using Docker Compose
############################

Docker provides utilities to simplify things with the use of Docker compose.
With Docker compose, we define a YAML file with all the instructions to launch our application and execute just as single command to run the application.

Lets create a ``docker-compose.yml`` file in the root of your repository with the instructions on how to run our application:

.. literalinclude:: reference/docker-compose.yaml
   :language: YAML

Lets now start our container with docker-compose using the following command:

.. code-block:: bash

   docker-compose up

The following is a sample output from the above command:

.. code-block::

   [cisco@centos HOLPRG-2002]$ docker-compose up
   Starting cl_app_1 ... done
   Attaching to cl_app_1
   app_1  | Watching for file changes with StatReloader


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
