from flask import Flask, request, make_response
from authomatic import Authomatic
from authomatic.adapters import WerkzeugAdapter

import config
import utils


app  = Flask(__name__)
app.debug = True
auth = Authomatic(config.auth,
                  utils.generate_oauth_secret()
                  )


@app.route('/api/login/<provider>')
def login(provider):

    response = make_response()
    
    app.logger.debug("login: got provider: {}".format(provider))
    result = auth.login(WerkzeugAdapter(request, response), provider)
    app.logger.debug("login: got result from auth: {}".format(result))

    return response
