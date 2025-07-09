FROM python:3.13-slim

WORKDIR /backend-dev

VOLUME [ "/backend-dev" ]

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["fastapi", "dev", "app.py", "--host", "0.0.0.0", "--port", "8000"]
