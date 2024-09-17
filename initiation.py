from flask import Flask
from flasgger import Swagger
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__, template_folder='./', static_folder='Statics')
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
limiter = Limiter(
    key_func = get_remote_address, 
    app = app,
    # default_limits=["100 per day", "10 per hour"]
)

Swagger(app)
