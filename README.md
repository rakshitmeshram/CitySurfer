# CitySurfer

CitySurfer is a location recommendation engine that generates recommendations for restaurants, cafes, parks, and tourist attractions based on user filters. The app uses the Google Maps API to collect data on various locations and offers a user-friendly interface to search and browse through the results.

## Features

- Search for places based on keywords and location
- Filter results by category, rating, and distance
- View detailed information for each place, including photos and reviews
- Get directions to the place using Google Maps
- Responsive design for mobile and desktop devices

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

