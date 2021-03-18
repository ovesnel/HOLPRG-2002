Step 4: Create Dockerfile
#########################

We will now create a `Dockerfile`, this is required in order for us to run our DJANGO application as a container (this ensures that we get the same result independent of the underlying operating system).

Copy the following code to a file called ``Dockerfile`` in the root of our repository.

.. literalinclude:: reference/Dockerfile
   :language: Dockerfile

After our Dockerfile is completed, we will need to create the ``requirements.txt`` referenced in our Dockerfile.

Lets create a ``requirements.txt`` in the root of our repository, with the following contents:

.. literalinclude:: reference/requirements.txt

We have specified two requirements, one is DJANGO, the other one which is requests will be needed when we need to query CSR1000v's APIs.
We will included it now to avoid having to rebuild our image later.
If anything changes in the ``requirements.txt`` file, we will have to rebuild our container.

.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
