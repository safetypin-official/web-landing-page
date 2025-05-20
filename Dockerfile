# filepath: c:\Users\fredo\Documents\FREDO2\PPL\web-landing-page\Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Create entrypoint script
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Use entrypoint script
ENTRYPOINT ["./entrypoint.sh"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]