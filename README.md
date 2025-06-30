# Django-REST-Framework

basic to advanced REST API by using python DRF

## live version

https://imdb-drf-api.onrender.com/swagger/

⚠️ Note: Since this backend is hosted on Render's free tier, the server may take up to 50 seconds to wake up after inactivity. You might encounter a temporary connection error — please wait and try again.

## Features

- Create, Read, Update and Delete Movies and Movie Reviews
- Token Authentication for API endpoints
- Admin Interface for data management

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start development server
```bash
python manage.py runserver
```

## API Endpoints

- `/api/movies/` - List all movies or create new
- `/api/movies/<int:id>/` - Retrieve, update or delete movie
- `/api/reviews/` - List all reviews or create new
- `/api/reviews/<int:id>/` - Retrieve, update or delete review
- `/api/auth/` - Get authentication token

## Technologies Used

- Django 4.x
- Django REST Framework
- SQLite3
- Python 3.x

