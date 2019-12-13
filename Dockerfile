FROM python:3.7-alpine

RUN apk update && \
    apk add --no-cache gcc musl-dev

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "controller.py" ]
