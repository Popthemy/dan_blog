# 📚 Story Publishing Platform - Dan Blog

Welcome to the **  Dan BlogStory Publishing Platform** 🎉 This is a simple platform where users can register, log in, and create, edit, and delete short stories. Built with **Django** and **Django REST Framework (DRF)**, this project is a mini MVP designed to showcase core functionality in a clean and modular way.

---

## 🚀 Features

- **User Authentication** 🔐
  - Register and log in with JWT-based authentication.
  - Secure password storage using Django's built-in hashing.

- **Story Management** ✍️
  - Create, edit, and delete stories.
  - View a list of all published stories.

- **RESTful API** 🌐
  - Fully functional API endpoints for all actions.
  - JSON responses for easy integration with frontend apps.

- **Testing** 🧪
  - Unit tests for 2 critical endpoints (login and delete story).

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Authentication**: JWT (Django Simple JWT)
- **Database**: SQLite (default development), PostgreSQL (production)
- **Environment Management**: Python Decouple
- **Testing**: Django Test Framework

---


## 🔧 Setup Instructions

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/story-platform.git
   cd story-platform
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory:
     ```bash
     SECRET_KEY=your_secret_key
     DEBUG=False
     DJANGO_SETTINGS_MODULE=story_platform.settings.prod  # For production
     DB_URL=your_db_link  # Optional for PostgreSQL
     ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the API**:
   - Visit `http://localhost:8000/api/` to interact with the API.

---

## 📄 API Documentation

### Endpoints

| Method | Endpoint               | Description                          |
|--------|------------------------|--------------------------------------|
| POST   | `/api/accounts/register/`       | Register a new user                  |
| POST   | `/api/accounts/login/`          | Log in and get JWT tokens            |
| GET    | `/api/stories/`        | Fetch all published stories          |
| POST   | `/api/stories/`        | Create a new story                   |
| PUT    | `/api/stories/{id}/`   | Edit a story (author only)           |
| DELETE | `/api/stories/{id}/`   | Delete a story (author only)         |
| GET | `/swagger/`   | Read documentation         |

### Example Requests

#### Register a User
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"pass123"}' http://localhost:8000/api/register/
```

#### Get JWT Tokens
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"pass123"}' http://localhost:8000/api/login/
```

---

## 🧪 Testing

We have tested the following endpoints:
1. **Login**: Ensures users can authenticate and receive JWT tokens.
2. **Delete Story**: Ensures authors can delete their stories.

Run the test suite:
```bash
python manage.py test
```

---

## 🚀 Deployment

### Local Development
- Use SQLite for simplicity. Just run the server with `python manage.py runserver`.

### Production
1. Use **PostgreSQL** as the database:
   - Update `DATABASES` in `settings.py`.
   - Install `psycopg2`: `pip install psycopg2-binary`.

2. Set up environment variables:
   - Add `SECRET_KEY`, `DEBUG=False`, and database credentials to `.env`.

3. Deploy to a platform like **Render**.

---

## 🤝 Contributing

Contributions are welcome! 🎉 Here's how you can help:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

---


## 🙏 Acknowledgments

- Django and DRF for the awesome backend framework.
- JWT for secure authentication.
- You, for checking out this project! ❤️

---

Enjoy building and sharing stories! 📖✨

---

### Sample `.env` File

```bash
# .env
SECRET_KEY=your_secret_key
DEBUG=False
DJANGO_SETTINGS_MODULE=story_platform.settings.prod  # For production
DB_URL=your_db_link  # Optional for PostgreSQL
```