# OpenNET API

OpenNET API - Nuttaphat

![opennet-api-nuttaphat](https://github.com/user-attachments/assets/f169eaca-2e81-4066-8ef8-4b2ee7620d17)

## Description

The OpenNET API (Home test - python engineer (SNR)) by Nuttaphat

## Project Directory Structure

```raw
opennet-api/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── greet_router.py
│   ├── models/
│   │   ├── response_model.py
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## API Endpoints

- [GET] /greet
  - query_param: user

## How to use

### Docker

```bash
docker-compose up
```

```bash
docker-compose up -d
```

### Manual

```bash
cd app
uvicorn main:app --reload
```
