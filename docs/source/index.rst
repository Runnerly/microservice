Myservice
=========


**myservice** is a simple JSON Flask application that uses **Flakon**.

The application is created with :func:`flakon.create_app`:

.. literalinclude:: ../../myservice/app.py


The :file:`settings.ini` file which is passed to :func:`create_app`
contains options for running the Flask app, like the DEBUG flag:

.. literalinclude:: ../../myservice/settings.ini
   :language: ini


Blueprint are imported from :mod:`myservice.views` and one
Blueprint and view example was provided in :file:`myservice/views/home.py`:

.. literalinclude:: ../../myservice/views/home.py
   :name: home.py
   :emphasize-lines: 13


Views can return simple mappings (as highlighted in the example above),
in that case they will be converted into a JSON response.

.. toctree::
   :maxdepth: 2

   api
