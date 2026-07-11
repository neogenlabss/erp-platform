FROM python:3.13-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN chmod +x entrypoint.sh

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT ["./entrypoint.sh"]