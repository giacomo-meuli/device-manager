FROM python:3.9-slim
RUN pip install "paho-mqtt<2.0"
COPY main.py /app/main.py
WORKDIR /app
CMD ["python", "main.py"]