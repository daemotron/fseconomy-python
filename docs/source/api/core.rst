.. _core:

Core
====

.. module:: fseconomy.core

.. warning::
   The functionality provided by the :mod:`fseconomy.core` module
   is reserved for internal purposes. It does not constitute an API
   intended for public use. This documentation is solely provided
   for the sake of completeness, and to support developers contributing
   to the :mod:`fseconomy` package.

API
---

.. module:: fseconomy.core.api

.. autodata:: API_VERSIONS
.. autodata:: MAINTENANCE
.. autodata:: DATA_FEEDS

Fetch Data Feed
---------------

.. module:: fseconomy.core.fetch

.. autofunction:: fetch

Keys
----

.. module:: fseconomy.core.keys

.. autodata:: ACCESS_KEY
.. autodata:: SERVICE_KEY
.. autodata:: USER_KEY

.. autofunction:: validate_key

.. autofunction:: get_data_keys

Server Response
---------------

.. module:: fseconomy.core.response

.. autoclass:: Response
   :members:
   :undoc-members:

Data Decoders
-------------

.. module:: fseconomy.core.data

Collection of data decoding functions to convert the raw XML data received
from the FSEconomy server into standard Python data types

.. autofunction:: fseconomy.core.data.aircraft.decode
.. autofunction:: fseconomy.core.data.aircraft.__decode_aircraft
