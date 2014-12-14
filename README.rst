===================
cbrf_rates
===================

cbrf_rates - это модуль для скачивания курсов валют с сайта cbr.ru (Центральный банк
Российской Федерации)

Лицензия MIT.

Зависимости
===========

* requests >= 2.5.0
* xmltodict >= 0.9.0

Установка
=========

Как обычно::

    $ pip install cbrf_rates

или ::

    $ easy_install cbrf_rates

или ::

    $ git clone https://github.com/moskrc/cbrf_rates.git
    $ cd cbrf_rates
    $ python setup.py install

Использование
=============

.. code-block:: python
    
    from cbrf_rates import get_rates1
    
    rates = get_rates()
    
    print rates['USD']
    
OrderedDict([(u'@ID', u'R01235'), (u'NumCode', u'840'), (u'CharCode', u'USD'), (u'Nominal', u'1'), (u'Name', u'Доллар США'), (u'Value', 56.8919)])

.. code-block:: python
    
    print rates['USD']['Value']

56.8919

.. code-block:: python
    
    print rates['date']

13.12.2014

