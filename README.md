# UCAR-TOPDOER-test

```pip install fastapi uvicorn SQLAlchemy pydantic```
```uvicorn main:app --reload```

# Примеры curl-запросов и их ответов.

запрос:
curl -X 'POST' \
  'http://127.0.0.1:8000/reviews' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "плохо"
}'

ответ:
{
  "id": 3,
  "text": "плохо",
  "sentiment": "negative",
  "created_at": "2025-07-08T18:58:08.078119"
}


запрос:
curl -X 'POST' \
  'http://127.0.0.1:8000/reviews' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "string"
}'

ответ:
{
  "id": 4,
  "text": "string",
  "sentiment": "neutral",
  "created_at": "2025-07-08T19:00:03.299762"
}


запрос:
curl -X 'POST' \
  'http://127.0.0.1:8000/reviews' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "хорош"
}'

ответ:
{
  "id": 5,
  "text": "хорош",
  "sentiment": "positive",
  "created_at": "2025-07-08T19:00:27.468404"
}


запрос:
curl -X 'GET' \
  'http://127.0.0.1:8000/reviews?sentiment=negative' \
  -H 'accept: application/json'

ответ:
[
  {
    "id": 3,
    "text": "плохо",
    "sentiment": "negative",
    "created_at": "2025-07-08T18:58:08.078119"
  }
]
