# YouTubeTime

A website where users can create profiles, share YouTube links, track screen time, and earn a share of ad revenue.

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`
7. Visit http://127.0.0.1:8000/ in your browser

## Features

- User registration and profiles
- YouTube video embedding
- Screen time tracking
- Ad integration with revenue sharing 