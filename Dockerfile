FROM python:3.9-slim
RUN pip install flask
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]