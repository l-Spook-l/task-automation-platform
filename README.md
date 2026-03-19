# Task Automation Platform

## 📌 Overview

This repository contains a set of backend tasks demonstrating:

* REST API development with FastAPI
* Background job processing with Celery + Redis
* Integration with external APIs
* Basic ML pipeline and API integration

The project is structured as a monorepo with three independent services.

---

## 📁 Project Structure

```
task-automation-platform/
│
├── task-automation-worker/  # Task 1 - Celery + External API
├── task-manager-api/        # Task 2 - REST API
├── task-ml-service/         # Task 3 - ML + Prediction API
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# ⚙️ Task 1 — Automation Worker (Celery + Redis)

### Description

Background job that:

1. Fetches users from external API
2. Transforms data
3. Saves it to CSV
4. Runs via Celery with Redis

---

## ▶️ Run with Docker

```bash
cd task-automation-worker
docker compose up -d --build
```

---

## 📡 Trigger job

```
POST /users/fetch-users
```

Response:

```json
{
  "task_id": "some-id",
  "status": "started"
}
```

---

## 📁 Output

```
task-automation-worker/data/users.csv
```

---

# 🚀 Task 2 — Task Manager API

### Description

RESTful API for managing tasks (to-do list).

### Features

* Get all tasks
* Create task
* Update task
* Delete task
* In-memory storage
* Input validation using Pydantic
* Unit tests

### Endpoints

| Method | Endpoint    | Description   |
| ------ | ----------- | ------------- |
| GET    | /tasks      | Get all tasks |
| POST   | /tasks      | Create task   |
| PUT    | /tasks/{id} | Update task   |
| DELETE | /tasks/{id} | Delete task   |

---

## ▶️ Run locally

```bash
cd task-manager-api
uv run uvicorn src.main:app --reload
```

## ▶️ Run with Docker

```bash
docker build -t task-manager-api -f task-manager-api/Dockerfile . 
docker run -d --name task-manager-api -p 8000:8000 task-manager-api 
docker stop task-manager-api
```


Docs:

```
http://localhost:8000/docs
```

---

## 🧪 Run tests

```bash
cd task-manager-api
pytest
```

---

# 🤖 Task 3 — ML Service

### Description

Simple ML pipeline for text classification:

* Input: task description
* Output: priority (high / low)

---

## ⚙️ Features

* Train model from CSV
* Save model to file
* Provide prediction via API

---

## ▶️ Train model

```bash
cd task-ml-service
uv run python -m src.ml.train_model
```

---

## ▶️ Run API

```bash
uv run uvicorn src.main:app --reload
```

## ▶️ Run with Docker

```bash
docker build -t task-ml-service -f task-ml-service/Dockerfile . 
docker run -d --name task-ml-service -p 8000:8000 task-ml-service 
docker stop task-ml-service
```

---

## 📡 Predict

```
POST /predict
```

Request:

```json
{
  "text": "Fix login bug"
}
```

Response:

```json
{
  "priority": "high"
}
```

---

## ⚡ Design Decisions

### Why no async?

Asynchronous programming was intentionally not used in most parts of this project.

**Reasoning:**

1. **Task 1** uses Celery, which already handles background processing and removes the need for async in the API layer.

2. **Task 2** works with in-memory data (no I/O operations), so async would not provide any performance benefit.

3. **Task 3:**
   - model inference is CPU-bound and fast
   - model training is CPU-bound and does not benefit from async

In all cases, adding async would increase complexity without improving performance.

---

## Developers
- https://github.com/l-Spook-l

## Contact

If you have any questions or suggestions for improving the project, please contact serhii.mykhailovskyi.ua@gmail.com.