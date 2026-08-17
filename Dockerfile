FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN  pip install psycopg2-binary
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]
