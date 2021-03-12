Step #1: Install Docker
#######################

As part of requirements Docker is needed, you can install it using the following commands:

.. code-block::

    #!/bin/bash

    # Install docker
    sudo yum check-update
    curl -fsSL https://get.docker.com/ | sh
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker $(whoami)


    
Sub-Title
---------



.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
