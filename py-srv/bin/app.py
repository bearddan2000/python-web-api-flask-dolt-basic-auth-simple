from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@db/animal"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class DogModel(db.Model):
    __tablename__ = 'dog'

    id = db.Column(db.Integer, primary_key=True)
    breed = db.Column(db.String())
    color = db.Column(db.String())

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

users = {
    'user': 'pass'
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return True
    return False

@app.route('/dog')
@auth.login_required
def handle_beverage():
        dogs = DogModel.query.all()
        results = [
            {
                "breed": dog.breed,
                "color": dog.color
            } for dog in dogs]

        return {"count": len(results), "dog": results, "message": "success"}


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
