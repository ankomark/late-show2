import csv
from app import app, db, Episode, Guest  # Import your models

def seed_data():
    with app.app_context():  # Wrap the database operations in an app context
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Open and read the CSV file
        with open('seed.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            episodes = []
            guests = set()  # Use a set to avoid duplicate guests

            for row in reader:
                # Create and collect episode data
                episode_date = row['Show']
                episode_number = len(episodes) + 1  # Just an example, adjust as necessary
                
                # Add episode
                episodes.append({
                    'date': episode_date,
                    'number': episode_number
                })

                # Add guest to the set (for uniqueness)
                guest_names = [name.strip() for name in row['Raw_Guest_List'].split(',')]
                for name in guest_names:
                    if name:  # Avoid empty names
                        guests.add((name, row['GoogleKnowledge_Occupation']))

        # Insert episodes into the database
        for episode in episodes:
            new_episode = Episode(
                date=episode['date'],
                number=episode['number']
            )
            db.session.add(new_episode)

        # Insert guests into the database
        for name, occupation in guests:
            new_guest = Guest(
                name=name,
                occupation=occupation
            )
            db.session.add(new_guest)

        db.session.commit()
        print("Database seeded!")

if __name__ == '__main__':
    seed_data()
