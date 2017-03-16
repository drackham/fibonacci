Development Environment
=========================================

Code Development
------------------------

Steps required to configure a debuggable, development environment:

All steps assume that you have a directory dedicated to the source from this project.  It can be anything so you should change DEV_HOME to your environment.

Pull the code for this project.

.. code:: console

          $ export DEV_HOME=$HOME/development/jarvis_mcmc
          $ mkdir -p $DEV_HOME
          $ cd $DEV_HOME/..
          $ git clone https://github.com/drackham/jarvis_mcmc.git
          $ cd $DEV_HOME

Create a local virtual environment

.. code:: console

          $ cd $DEV_HOME/jarvis_mcmc_api
          $ virtualenv --no-site-packages python
          $ source python/bin/activate               # ensure you are using the correct virtualenv python
          $ pip install --upgrade pip
          $ pip install -r requirements.txt

Run flask to start the application and debug as appropriate.  You can set breakpoints as needed.

.. code:: console

          $ python main.py


Use Curl to pull results

.. code:: console

          $ curl http://$DOCK_IP/jarvis_mcmc/sim/sir-thomas
          {
            "box": "sir-thomas",
            "chains": 4,
            "dataset": "foo.RData",
            "id": 1,
            "iter": 2000,
            "max_cores": 4,
            "model": "foo.model",
            "n": 1000,
            "results_path": "foo/bar"
          }


Documentation Development
----------------------------------------

To update docs after building, run the Sphinx makefile:

.. code:: console

          $ cd $DEV_HOME/jarvis_mcmc_api/docs
          $ make html

Generated documentation appears in $DEV_HOME/jarvis_mcmc_api/static

Provided that docs have been generated with their makefile, they can be viewed in a running instance by directing your browser to:

http://localhost:5000/jarvis_mcmc/docs



Testing
----------------------

Tests utilize Nose for managing the tests.

To add tests, stick with the naming convention and create a module suffixed with "_test.py" and prefixed with the module you are testing.  See "jarvis_mcmc_test.py" for example.

To execute tests:

.. code:: console

          $ cd $DEV_HOME/jarvis_mcmc_api
          $ nosetests
          .....
          ----------------------------------------------------------------------
          Ran 5 tests in 0.020s

          OK


To execute tests and generate coverage information:

.. code:: console

          $ nosetests --with-coverage --cover-html --cover-package=jarvis_mcmc_api --cover-erase
          .....

          Name                         Stmts   Miss  Cover   Missing
          ----------------------------------------------------------
          fibonacci_api.py                 0      0   100%
          fibonacci_api/common.py          5      0   100%
          fibonacci_api/fibonacci.py      13      0   100%
          fibonacci_api/main.py           28      4    86%   20, 48-49, 70
          ----------------------------------------------------------
          TOTAL                           46      4    91%

          ----------------------------------------------------------------------
          Ran 5 tests in 0.025s

          OK



Coverage output is available in HTML format in the $DEV_HOME/jarvis_mcmc_api/cover directory.  This information is not stored in GIT.
