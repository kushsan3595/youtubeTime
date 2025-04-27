# YouTubeTime Setup Instructions

## Overview

YouTubeTime is a platform where users can:
- Create profiles
- Share YouTube videos
- Track their screen time
- Earn rewards from ad revenue

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd youtubeTime
```

### 2. Create and Activate Virtual Environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Database

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 6. Create Media Directory

Ensure the media directory exists for user uploads:

```bash
mkdir -p media/avatars
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to access the site.

### 8. Admin Access

Visit http://127.0.0.1:8000/admin/ and log in with your superuser credentials to manage the site.

## Features Implementation

### User Profiles
- Users can register, log in, and create profiles
- Profiles display YouTube videos shared by the user
- Users can upload profile pictures

### YouTube Videos
- Users can add YouTube videos by pasting YouTube links
- The system automatically extracts YouTube IDs for embedding
- Videos can be edited or deleted by their owners

### Screen Time Tracking
- The system tracks how long users spend on the site
- A middleware records user activity sessions
- The navbar displays a real-time counter

### Ad Revenue
- Ad impressions and clicks are tracked
- Users earn a small amount for each ad impression/click
- Earnings are displayed on the user dashboard

## Production Deployment

For production, make sure to:

1. Set `DEBUG = False` in settings.py
2. Configure a proper database (PostgreSQL recommended)
3. Set up proper email backend for account verification
4. Update `SECRET_KEY` to a unique, secure value
5. Configure static files serving
6. Set up HTTPS with proper SSL certificate 