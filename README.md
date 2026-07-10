# Student OS

Student OS is a college management platform built using Django and React. It provides authentication, student and faculty management, subjects, class schedules, notifications, and other academic services.

---

## Project Overview

Student OS is designed to provide:

* Google Single Sign-On (SSO)
* Student and Faculty Management
* Subject Management
* Class Scheduling
* Notification System
* Responsive Web Interface

---

## Technology Stack

* Python
* Django
* Django REST Framework
* React
* Vite
* Tailwind CSS
* SQLite (Development)
* PostgreSQL (Production)
* Git and GitHub

---

## Installation Steps

### Clone Repository

```bash
git clone https://github.com/Narottamrout/student-os.git
cd student-os
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Backend

```bash
python manage.py runserver
```

Backend URL:

```text
http://127.0.0.1:8000/
```

---

## Running Frontend

Go to frontend folder:

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173/
```

---

## Project Structure

```text
student_os/
├── frontend/
├── student_os/
├── accounts/
├── academics/
├── notifications/
├── api_app/
├── manage.py
├── requirements.txt
└── README.md
```

---

## API Information

### Hello Endpoint

```text
GET /api/hello/
```

Response:

```json
{
  "message": "Student OS Backend Running Successfully 🚀"
}
```

### Planned APIs

```text
GET    /api/me/
GET    /api/subjects/
GET    /api/classes/today/
GET    /api/notifications/
POST   /api/notifications/create/
PATCH  /api/notifications/<id>/read/
```

---

## Week 1 Deliverables

* Repository Setup
* README Documentation
* Coding Standards
* Hello World Django Endpoint
* Tailwind Shell Rendering on Localhost

---

## Author
spine group
Student OS Project
