from flask import Flask, jsonify, request, make_response, redirect, url_for, session
from flask_login import LoginManager
from flask_cors import CORS
from view import blog
from control.user_control import User
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'wkkim_server'

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@app.route('/')
def index():
    print('index')
    return redirect(url_for('blog.blog_home'))

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

@app.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5555')
