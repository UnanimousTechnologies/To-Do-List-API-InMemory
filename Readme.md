### Build a To-Do App with FastAPI and CRUD Operations in Python
FastAPI is one of the fastest and most modern Python web frameworks today. If you want to build APIs, learning FastAPI CRUD operations is a must. In this blog, we will go step by step to create a simple To-Do App using FastAPI and then connect it with a frontend.

## What is FastAPI?
FastAPI is a lightweight and high-performance web framework built on Python 3.7+ with support for async/await.
Key Features:
Super fast performance (built on Starlette and Pydantic)


## Automatic API documentation with Swagger UI and ReDoc


# 1. Easy validation with Pydantic models


# 2. Beginner-friendly and widely used in production

What is CRUD in FastAPI?
CRUD stands for:
Create → Add new records

Read → Retrieve records

Update → Modify existing records

Delete → Remove records


### For our To-Do App, we will implement these four operations.

## Step 1: Install FastAPI and Uvicorn

pip install fastapi uvicorn

## Step 2: Create FastAPI App (main.py)

Run the server with:

uvicorn main:app --reload

Now, open your browser at:
API docs → http://127.0.0.1:8000/docs

## Step 3: Connect with a Simple Frontend (index.html):

Serve index.html over HTTP (don’t open file:// directly):

python -m http.server 5500


Open http://127.0.0.1:5500


## Final Thoughts
FastAPI makes it super easy to build APIs with full CRUD support. By combining it with a simple frontend, you can create powerful apps quickly. In this tutorial, we built a To-Do List app using FastAPI and CRUD operations.

