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
