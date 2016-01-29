from flask import Flask, request, make_response
from authomatic import Authomatic
from authomatic.adapters import WerkzeugAdapter

import config
import utils


app  = Flask(__name__)
auth = Authomatic(config.auth,
                  utils.generate_oauth_secret()
                  )


@app.route('/login/<provider>')
def login(provider):

    response = make_response()

    result = auth.login(WerkzeugAdapter(request, response), provider)


