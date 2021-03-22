Step 4: Create Dockerfile
#########################

We will now create a `Dockerfile`, this is required to run our Django application as a container (this ensures that we get the same result independent of the underlying operating system).

Copy the following code to a file called :guilabel:`Dockerfile` in the root of our repository.

.. literalinclude:: reference/Dockerfile
   :language: Dockerfile
   :caption: Dockerfile
   :linenos:

After our Dockerfile is completed, we will need to create the :guilabel:`requirements.txt` file referenced in our Dockerfile.

Let's create a :guilabel:`requirements.txt` in the root of our repository, with the following contents:

.. literalinclude:: reference/requirements.txt
   :caption: requirements.txt
   :linenos:

We have specified two requirements, one is Django, the other one which is requests will be needed to query the CSR1000v's APIs.
We will included it now to avoid having to rebuild our image later.
If anything changes in the :guilabel:`requirements.txt` file, we will have to rebuild our Docker image.

.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
