Step 1: Add Static Files for Cisco UI Kit
#########################################

Copy the directory named ``static`` at the root of the repository to your netprog directory.
When copied, the directory should look like the output of the below command:

.. TODO::

    Explain the origin of the static folder

.. code-block:: bash

    root@ec8da46bb441:/app# ls -la
    total 8
    drwxr-xr-x  7 root root  224 Mar 18 17:56 .
    drwxr-xr-x  1 root root 4096 Mar 18 17:51 ..
    -rw-r--r--  1 root root    0 Mar 18 15:12 db.sqlite3
    drwxr-xr-x 12 root root  384 Mar 18 17:43 interfaces
    -rwxr-xr-x  1 root root  663 Mar 18 17:33 manage.py
    drwxr-xr-x  8 root root  256 Mar 18 17:36 netprog
    drwxr-xr-x  6 root root  192 Mar 18 17:56 static


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
