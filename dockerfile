FROM python:3.10-alpine3.20 AS base

WORKDIR /app

COPY . /app/

RUN apk update
RUN apk add libpq

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3"] 
CMD ["secretnote/manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

