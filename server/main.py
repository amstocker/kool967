from flask import Flask, request, make_response
from authomatic import Authomatic
from authomatic.adapters import WerkzeugAdapter
import json

import config
import utils


app  = Flask(__name__)
app.debug = True
auth = Authomatic(config.auth,
                  utils.load_oauth_secret()
                  )


@app.route('/api/login/<provider>')
def login(provider):

    response = make_response()
    
    result = auth.login(WerkzeugAdapter(request, response), provider)

    app.logger.debug("login: got result: {}".format(result))

    if result and result.error:
        return result.error.message

    if result and result.user:
        return json.dumps({'name' : result.user.name,
                           'id' : result.user.id,
                           'email' : result.user.email})

    return response
