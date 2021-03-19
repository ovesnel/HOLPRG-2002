Step 5: Activate Application
############################

To include the app in our project, we need to add a reference to its configuration class in the **INSTALLED_APPS** setting. The Config class is in the ``interfaces/apps.py`` file, so its dotted path is 'interfaces.apps.interfacesConfig'. Edit the ``netprog/settings.py`` file and add that dotted path to the INSTALLED_APPS setting. It’ll look like this:

.. code-block:: Python
    :caption: netprog/settings.py
    :emphasize-lines: 8

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'interfaces.apps.InterfacesConfig',
    ]


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
