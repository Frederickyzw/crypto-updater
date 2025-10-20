# Gunakan image Python resmi
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy semua file ke container
COPY . .

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan FastAPI menggunakan uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
