# Building a To-Do List API with FastAPI

In this guide, we will create a simple To-Do List API using FastAPI and walk through the process step by step.

## Getting Started

### Prerequisites

Before you begin, make sure you have Python, FastAPI, and Uvicorn installed. You can install them using pip:

```bash

pip install fastapi uvicorn

```

### Setting Up the Project

1. Create a new directory for your project.

2. Inside the project directory, create a Python file (e.g., main.py) to define your FastAPI app.

3. Create a virtual environment and activate it:

```bash

python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

```

Install FastAPI and Uvicorn inside the virtual environment.

### Creating the FastAPI App

Open **'main.py'** and define your FastAPI app. Here's a basic example:

```python

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do List API"}

```

### Running the App

You can run your FastAPI app using Uvicorn. Execute the following command from the project directory:

```bash

uvicorn main:app --reload

```

Your FastAPI app will be available at **'<http://127.0.0.1:8000>'**.

### Creating API Endpoints

Now, let's create endpoints to manage a to-do list.
Creating a To-Do

To create a new to-do item, make a POST request to /todos/ with a JSON body:

```http

POST <http://127.0.0.1:8000/todos/>
{
    "todo": "Buy groceries"
}
```

### Getting All To-Dos

To retrieve all to-do items, make a GET request to /todos/:

```http

GET <http://127.0.0.1:8000/todos/>

```

### Getting a Specific To-Do

To retrieve a specific to-do item, make a GET request to /todos/{todo_id}:

```http

GET <http://127.0.0.1:8000/todos/0>

```

### Deleting a To-Do

To delete a specific to-do item, make a DELETE request to /todos/{todo_id}:

```http

DELETE <http://127.0.0.1:8000/todos/0>

```

### API Documentation

FastAPI generates interactive API documentation for you. You can access it at:

Swagger UI
ReDoc

#### API End-Pont Docs

FastAPI automatically generates interactive documentation for your API. You can access it at **'<http://127.0.0.1:8000/docs>'** or **'<http://127.0.0.1:8000/redoc>'**. This documentation is very useful for testing and exploring your API.

These documentation tools make it easy to test and explore your API endpoints.
Conclusion

Congratulations! You've built a simple To-Do List API using FastAPI. You can further enhance this project by adding more features and improving the code structure.
