from nose.tools import ok_, eq_
from flask import json
import main

test_app = main.app.test_client()


STATUS_OK = 200
STATUS_REDIR = 302
STATUS_CLIENT_ERROR = 403

def test_jarvis_mcmc_docs():
    """
    function:  test_jarvis-mcmc_docs
    notes:     Ensure that /jarvis-mcmc/docs redirects to the right place
    """
    resp = test_app.get('/jarvis_mcmc/docs')
    eq_(resp.status_code, STATUS_REDIR, "Response code %s is not != %s for /jarvis-mcmc/docs redirection" % (resp.status_code, STATUS_REDIR))

def test_index():
    """
    function: test_index
    notes: Ensure that the index redirects to the documentation
    """
    resp = test_app.get('/')
    page = "http://localhost/static/index.html"
    
    eq_(resp.status_code, STATUS_REDIR, "Response code %s != %s for / redirection" % (resp.status_code, STATUS_REDIR))
    eq_(resp.location, page, "Page URL %s is not %s" % (resp.location, page))

def test_sim_no_box_api():
    """
    function: test_sim_no_box_api
    notes: Ensure the API responds correctly when no sim box is specified
    """
    resp = test_app.get('/jarvis_mcmc/sim/')
    eq_(resp.status_code, STATUS_CLIENT_ERROR, "Response code %s != %s for /jarvis_mcmc/sim" % (resp.status_code, STATUS_CLIENT_ERROR))