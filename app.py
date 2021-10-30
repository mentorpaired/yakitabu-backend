import os
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
# db = SQLAlchemy(app)

app.config.from_object('config')
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id=app.config["GOOGLE_CLIENT_ID"],
    client_secret=app.config["GOOGLE_CLIENT_SECRET"],
    access_token_url='https://accounts.google.com/o/oauth2/token',
    # access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    # authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',

    # This is only needed if using openId to fetch user info
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    
    # https://auth0.com/docs/configure/apis/scopes/openid-connect-scopes
    client_kwargs={
        'scope': 'openid email profile'
    },
)


# Google login route
@app.route('/login/google')
def google_login():
    _google = oauth.create_client('google')
    redirect_uri = url_for('google_authorize', _external=True)
    return _google.authorize_redirect(redirect_uri)


# Google authorize route
@app.route('/login/google/authorize')
def google_authorize():
    google_client = oauth.create_client('google')
    token = google_client.authorize_access_token()
    response = google_client.get('userinfo').json()
    return response


@app.route("/")
def hello_world():
    return "<p> Hello World.! </p>"


if __name__ == '__main__':
    app.run()
