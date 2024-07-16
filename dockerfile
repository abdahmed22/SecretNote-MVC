# base stage that copy files and builds them

FROM python:3.10-alpine3.20 AS base

WORKDIR /app

COPY . /app/

RUN apk update
RUN apk add libpq

RUN pip install --no-cache-dir -r requirements.txt


# run stage that run binaries
FROM python:3.10-alpine

RUN apk add libpq

COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY . /app

ENTRYPOINT ["python3"] 
CMD ["secretnote/manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

