FROM python:3.10-alpine

WORKDIR /app

RUN apk update && apk upgrade --no-cache
RUN apk add --no-cache tzdata
ENV TZ=Asia/Ho_Chi_Minh

COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app

# ENTRYPOINT ["python"]
# CMD ["minio_api.py"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "minio_api:app"]
