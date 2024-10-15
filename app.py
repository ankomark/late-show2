from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nyambura:nyambura@localhost:5432/late_show'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# Define your models
class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number
        }

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    episode = db.relationship('Episode', backref='appearances')
    guest = db.relationship('Guest', backref='appearances')

    def serialize(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'episode_id': self.episode_id,
            'guest_id': self.guest_id,
            'episode': self.episode.serialize(),
            'guest': self.guest.serialize()
        }

# Function to create the database tables
def create_db():
    with app.app_context():
        db.create_all()

# Call the create_db function to create tables
create_db()

# Define your routes
@app.route('/')
def index():
    return "Welcome to the Late Show API!"

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.serialize() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    
    appearances = Appearance.query.filter_by(episode_id=id).all()
    serialized_appearances = [appearance.serialize() for appearance in appearances]

    return jsonify({
        'id': episode.id,
        'date': episode.date,
        'number': episode.number,
        'appearances': serialized_appearances
    })

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.serialize() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    if not data or 'rating' not in data or 'episode_id' not in data or 'guest_id' not in data:
        return jsonify({"errors": ["validation errors"]}), 400

    new_appearance = Appearance(
        rating=data['rating'],
        episode_id=data['episode_id'],
        guest_id=data['guest_id']
    )

    db.session.add(new_appearance)
    db.session.commit()

    return jsonify(new_appearance.serialize()), 201

if __name__ == '__main__':
    app.run(debug=True, port=5555)
