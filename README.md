# FastAPI Student CRUD API

This is a simple RESTful API built with the FastAPI framework that supports basic CRUD operations (Create, Read, Update, Delete) for a Student entity. The Student entity has the following attributes:

\- ID: (Integer)

\- Name: (String)

\- Grade: (String)

\- Email: (String)

## Project Structure

. ├── main.py

  ├── models.py 

  ├── schemas.py

  ├── database.py

  ├── requirements.txt

  └── README.md

## Environment Setup

### 1. Clone the Project

```sh
git clone <repository_url>
cd <repository_directory>
```

### 2. Create a Virtual Environment

Create and activate a virtual environment in the project root directory:

```shell
python3 -m venv venv

source venv/bin/activate # Linux/macOS

venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure the Database

In the `database.py` file, configure your MySQL database connection:

`DATABASE_URL = "mysql+pymysql://<username>:<password>@<host>/<database_name>"`

Ensure you have created the corresponding database in MySQL.

## Running the Service

### 1. Start the FastAPI Application

`uvicorn main:app --reload`

### 2. Access the API Documentation

Open your browser and visit `http://127.0.0.1:8000/docs` to see an interactive Swagger UI where you can test all the API endpoints.

## API Endpoints

- `GET /students/`: Retrieve a list of all students.
- `GET /students/{id}`: Retrieve details of a student by ID.
- `POST /students/`: Add a new student.
- `PUT /students/{id}`: Update an existing student by ID.
- `DELETE /students/{id}`: Delete a student by ID.

## Dependencies

- fastapi
- uvicorn
- sqlalchemy
- pymysql

## Contributing

Contributions are welcome! Please fork this repository and submit a PR.