from flask import Flask, render_template
from flask_migrate import Migrate

from .config import Config
from .models import db
from .routes import home, new_package

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(home.bp)
app.register_blueprint(new_package.bp)
