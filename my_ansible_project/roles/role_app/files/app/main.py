from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://"
    f"{os.environ.get('DB_USER')}:"
    f"{os.environ.get('DB_PASSWORD')}@"
    f"{os.environ.get('DB_HOST')}:5432/"
    f"{os.environ.get('APP_NAME', 'my_ansible_app')}_db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_world():
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER', 'guest')
    db_password_present = "yes" if 'DB_PASSWORD' in os.environ else "no"
    app_debug_mode = os.environ.get('FLASK_ENV', 'production') == 'development'

    db_connection_status = "N/A"
    try:
        db.session.execute(db.text("SELECT 1"))
        db_connection_status = "Connected"
    except Exception as e:
        db_connection_status = f"Failed ({str(e)})"

    return jsonify({
	"message": f"Hello from {os.environ.get('INVENTORY_HOSTNAME', 'unknown')}! This is {os.environ.get('APP_NAME', 'my_ansible_app')} ({os.environ.get('APP_VERSION', '1.0')})!",
        "environment": app_debug_mode,
        "db_connection": {
            "host": db_host,
            "user": db_user,
            "password_present": db_password_present,
	    "status": db_connection_status
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
