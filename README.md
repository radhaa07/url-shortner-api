# URL Shortener API

## Project Description

This project is a simple URL Shortener API built using FastAPI and PostgreSQL. It allows users to submit a long URL and receive a shortened URL. When the shortened URL is accessed, the API redirects the user to the original URL.

---

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- python-dotenv

---

## Project Structure

```
url-shortner_API/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the project

```bash
git clone <repository_url>
```

### Move into the project folder

```bash
cd url-shortner_API
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

1. Install PostgreSQL.
2. Create a database.
3. Create a `.env` file using `.env.example`.

Example:

```text
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/url-shortner
```

---

## Run the Project

```bash
uvicorn app.main:app --reload
```

Server runs on:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### POST /shorten

Request

```json
{
    "long_url": "https://www.google.com"
}
```

Response

```json
{
    "short_url": "http://localhost:8000/Ab12Cd"
}
```

---

### GET /{short_code}

Example

```
GET /Ab12Cd
```

Redirects the user to the original URL.

---

## Features

- Generate short URLs
- Store URLs in PostgreSQL
- Redirect using short code
- Input validation using Pydantic
- Proper HTTP error handling
- Environment variable configuration

---

## Author

Radha Waghmare
