# FastAPI ilovasini Docker konteynerida ishlatish uchun Dockerfile

# Pythonning rasmiy imajidan foydalanamiz
FROM python:3.9-slim

# Ishlash katalogini yaratamiz
WORKDIR /app

# requirements.txt faylini konteynerga nusxalash
COPY requirements.txt .

# Kerakli paketlarni o'rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Ilova fayllarini konteynerga nusxalash
COPY . /app

# Portni ochish
EXPOSE 8000

# Uvicorn serverini ishga tushurish
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
