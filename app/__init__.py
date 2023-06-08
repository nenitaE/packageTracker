from flask import Flask, render_template

from .config import Config
# from .models import db
from .routes import home, new_package

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(home.bp)
app.register_blueprint(new_package.bp)
