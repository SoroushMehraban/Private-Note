FROM python:3.8.5-alpine as base

RUN pip install --upgrade pip

RUN apk add build-base

COPY ./requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.8.5-alpine

COPY ./app /app
COPY --from=base /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/

WORKDIR /app

RUN adduser -D user
USER user

