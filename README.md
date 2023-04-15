# CitySurfer - A Location Recommendation Engine

CitySurfer is a machine learning-powered location recommendation engine that helps users discover new and interesting locations in a city. The application collects data on various locations such as restaurants, cafes, parks, and tourist attractions using the Google Maps API and generates recommendations based on user preferences and filters. The backend of the application is built with Django and Firebase, and the frontend is styled using the Tailwind CSS framework.

## Features

CitySurfer has several features that make it a useful tool for exploring a city:

- Personalized recommendations based on user preferences
- Filters for refining search results based on category, rating, and popularity
- Integration with Google Maps for easy navigation to recommended locations
- User authentication and profile management for personalized experiences
- Admin panel for managing location data and user accounts

## Technical Details
The backend of CitySurfer is built with Django, a high-level Python web framework. Django provides a robust and secure foundation for building web applications, and is known for its scalability and flexibility. Firebase, a cloud-based mobile and web application development platform, is used as a backend service for handling user authentication and data storage.

The machine learning model used in CitySurfer is a collaborative filtering algorithm that recommends locations based on the user's past behavior and preferences. The model is trained on a dataset of location ratings and reviews, and is updated in real-time as users interact with the application.

The frontend of CitySurfer is styled using Tailwind CSS, a utility-first CSS framework that makes it easy to rapidly prototype and customize the appearance of the application. The user interface is designed to be intuitive and user-friendly, with a focus on simplicity and ease of use.

## Requirements

- Python 3.6 or higher
- Django 3.2.8 or higher
- Google Maps API key
- See requirements.txt for additional dependencies

## Installation

1. Clone the repository:

```
git clone https://github.com/RakshitMeshram/city-surfer.git
cd city-surfer
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Set up the database:

```
python manage.py migrate
```


4. Set up the Google Maps API key:

- Create a new project in the [Google Cloud Console](https://console.cloud.google.com/)
- Enable the Maps JavaScript API and the Places API
- Create a new API key with the appropriate restrictions
- Add the API key to your environment variables or update the `GOOGLE_MAPS_API_KEY` variable in `city_surfer/settings.py`

5. Run the development server:

```
python manage.py runserver
```

6. Access the app in your web browser at `http://localhost:8000/`

## Project Structure

- `city_surfer/`: Django project settings and configuration
- `main/`: Django app for the main functionality of the app
- `models.py`: Django models for the app's database tables
- `urls.py`: Django URL configuration for the app's views
- `views.py`: Django views for handling user requests and rendering templates
- `templates/`: HTML templates for the app's pages
- `static/`: Static files for the app's styles and images
- `manage.py`: Django command-line utility for managing the app
- `requirements.txt`: List of Python dependencies required to run the app
- `.gitignore`: List of files and directories to ignore by Git
- `README.md`: This file

## Folder Tree

```
city_surfer/
├── city_surfer/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── locations/
│   ├── templates/
│   │   ├── location_detail.html
│   │   ├── location_list.html
│   │   └── base.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── templates/
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── register.html
│   │   └── base.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   ├── app.css
│   │   └── tailwind.css
│   ├── images/
│   └── js/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── search_results.html
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

## License

CitySurfer is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

