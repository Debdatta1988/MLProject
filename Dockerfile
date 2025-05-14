FROM python:3.13-slim
WORKDIR /app
COPY . /app/
RUN apt update && apt install awscli -y

RUN pip install -r requirements.txt
CMD ["python", "app.py"]