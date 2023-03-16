# MalCheck-Server
Malware Automation Check server


## 1. Capabilities
- Dashboard for data visualization and user tracking: check-in, check-out.
- MalCheck Proxy for S3/MinIO/Ceph Storage.


## 2. Deployment

- Clone source:
```bash
$ git clone https://github.com/hailehong95/malcheck-server.git
$ cd malcheck-server
```

- Copy and edit `.env` file
```bash
$ cp .env.example .env
```

- File example
```
DASH_USER = "ChangeMe"
DASH_PASSWORD = "ChangeMe"
SECRET_KEY = "ChangeMe"
CHAT_ID = ChangeMe
BOT_TOKEN = ChangeMe
MINIO_HOST = "ChangeMe"
MINIO_ACCESS_KEY = "ChangeMe"
MINIO_SECRET_KEY = "ChangeMe"
MINIO_BUCKET_NAME = "ChangeMe"
```


- Using docker-compose to deploy:
```bash
$ docker-compose up -d
```

## 3. Checking
```bash
$ docker-compose ps -a
$ docker-compose logs -f
$ tail -f data/logs/dash.log
```
