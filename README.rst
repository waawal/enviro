.. image:: http://media.giphy.com/media/gBxL0G0DqZd84/giphy.gif
    :alt: Environment Friendly!
    :align: left
    :target: https://pypi.python.org/pypi/enviro

enviro
======

**enviro lets you set default values of** ``os.environ`` **from a configuration file.** This can be useful if you want to be able to override parts of your configuration based on the running environment. Using this approach is ideal for when you want your configuration to play nicely with PaaS services.

....

Usage
-----

Populating your Default Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from enviro import setdefault
    setdefault('mysettings.conf')

....

`enviro` will now look in the following directories for a file called ``mysettings.conf``:

1. Current Working Directory ``cwd``
2. Home directory ``$HOME``
3. ``/etc``
4. The path of the executed script. ``__file__`` of ``__main__``

....

.. code:: python

    import os
    import enviro
    enviro.setdefault('mysettings.conf')

    os.environ['foodir']
    # Will give you 'frob/whatever' based on the example config below.

If ``foodir`` was already defined in the environment, `enviro` would not have overwritten it.

Configuration File Format
~~~~~~~~~~~~~~~~~~~~~~~~~

The configuration file is in normal ``.ini`` format *without section headers*. It supports interpolation as you would expect.

::

    foodir: %(dir)s/whatever
    dir=frob
    long: this value continues
       in the next line

Installation
------------

Install *enviro* with pip:

::

    $ pip install enviro


License
-------

GPL v.2

.. image:: http://i.imgur.com/Bp9pZ4k.jpg

