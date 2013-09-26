enviro
======

.. image:: http://media.giphy.com/media/gBxL0G0DqZd84/giphy.gif
    :alt: Environment Friendly!
    :align: left
    :target: https://pypi.python.org/pypi/enviro

Environmentally Friendly Configuration

`enviro` lets you and your users set default values of os.env from a file.

Example
-------

.. code:: python

    from enviro import environment
    environment('mysettings.conf')

`enviro` will now look in the following directories for a file called `mysettings.conf`:

1. Current Working Directory (cwd)
2. $HOME
3. /etc
4. The path of the executed script.

Installation
------------

Install *enviro* with pip:

::

    $ pip install enviro


License
-------

GPL v.2