.. include:: <isonum.txt>

================================================
    Pyak47 | Performance Test Framework
================================================

|

.. image:: assets/graphs.png

----

:Dev: `Pyak47 source <https://github.com/kakwa/pyak47>`_
:PyPI: `Pyak47 package <http://pypi.python.org/pypi/pyak47>`_
:License: `GNU LGPLv3 <http://www.gnu.org/licenses/lgpl.html>`_
:Author: Pierre-Francois Carpentier - copyright |copy| 2014

----

:Original author: `Corey Goldberg <http://goldb.org>`_ - copyright |copy| 2010-2013
:Original project: `multimechanize.com <http://multimechanize.com>`_

----

**************************************
    Performance & Load Tests in Python
**************************************

Pyak47 is an open source framework for performance and load testing. 
It runs concurrent Python scripts to generate load (synthetic transactions) 
against a remote site or service.

Pyak47 is most commonly used for web performance and scalability 
testing, but can be used to generate workload against any remote API accessible 
from Python.

Test output reports are saved as HTML or JMeter-compatible XML.

*************
    Site Menu
*************

.. toctree::
    :maxdepth: 1
    
    setup
    configfile
    scripts
    reports
    datastore
    dev
    changelog
    
*******************************
    Discussion / Help / Updates
*******************************

* IRC: `Freenode <http://freenode.net/>`_ ``#pyak47`` channel
* Bugtracker: `Github <https://github.com/kakwa/pyak47/issues>`_

*******************
    Install / Setup
*******************

Pyak47 can be installed from `PyPI <http://pypi.python.org/pypi/pyak47>`_ using `pip <http://www.pip-installer.org>`_::
    
    pip install -U pyak47

... or download the `source distribution from PyPI <http://pypi.python.org/pypi/pyak47#downloads>`_, unarchive, and run::

    python setup.py install

(for more setup and installation instructions, see :ref:`setup-label`)

**********************
    Usage Instructions
**********************

--------------------
    Create a Project
--------------------

Create a new test project with ``pyak47-newproject``::

    $ pyak47-newproject my_project

Each test project contains the following:

 * ``config.cfg``: configuration file. set your test options here.
 * ``test_scripts/``: directory for virtual user scripts. add your test scripts here.
 * ``results/``: directory for results storage. a timestamped directory is created for each test run, containing the results report.

``pyak47-newproject`` will create a mock project, using a single script that generates random timer data.  Check it out for a basic example. 

-----------------
    Run a Project
-----------------

Run a test project with ``pyak47-run``::

    $ pyak47-run my_project

* for test configuration options, see :ref:`config-label`
* a timestamped ``results`` directory is created for each test run, containing the results report.

************************
    Test Scripts
************************

--------------------------
    Virtual User Scripting
--------------------------

* written in Python
* test scripts simulate virtual user activity against a site/service/api
* scripts define user transactions
* for help developing scripts, see :ref:`scripts-label`

------------
    Examples
------------

HTTP GETs using `Requests <http://docs.python-requests.org/>`_::

    import requests

    class Transaction(object):
        def run(self):
            r = requests.get('https://github.com/timeline.json')
            r.raw.read()

HTTP GETs using `Mechanize <http://wwwsearch.sourceforge.net/mechanize/>`_ (with timer and assertions)::

    import mechanize
    import time

    class Transaction(object):
        def run(self):
            br = mechanize.Browser()
            br.set_handle_robots(False)
            
            start_timer = time.time()
            resp = br.open('http://www.example.com/')
            resp.read()
            latency = time.time() - start_timer
            
            self.custom_timers['Example_Homepage'] = latency
            
            assert (resp.code == 200)
            assert ('Example Web Page' in resp.get_data())

----

.. image:: assets/python-powered.png
