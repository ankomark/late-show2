# Late Show API

This project is a RESTful API for managing episodes, guests, and their appearances on a late-night show. It is built using Flask and SQLAlchemy, with PostgreSQL as the database.

## Features

- Retrieve a list of episodes
- Retrieve details for a specific episode, including guest appearances
- Retrieve a list of guests
- Add guest appearances with ratings

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Flask-SQLAlchemy**: An ORM for Flask applications that provides a SQL toolkit.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Python**: The programming language used for the application.

## Installation

### Prerequisites

- Python 3.6 or higher
- PostgreSQL
- pip

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/annewaithaka/late-show.git
   cd late_show_api

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
pip install -r requirements.txt

4. Update the database URI in app.py if necessary:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/late_show'

5. Create the database tables:
python app.py
Usage

6. Start the application:
python app.py

The API will be available at http://localhost:5555/.

### Endpoints
GET / - Welcome message
GET /episodes - List all episodes
GET /episodes/<id> - Get a specific episode by ID
GET /guests - List all guests
POST /appearances - Create a new guest appearance

### Contributing
Fork the repository.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.