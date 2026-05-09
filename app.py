from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL connection
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://nabila@localhost:5432/nabila"

db = SQLAlchemy(app)


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route("/")
def home():
    return "PostgreSQL is connected successfully!"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        app.run(debug=True)
