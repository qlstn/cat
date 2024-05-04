FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 intsall --no-cache-dir --upgrade -r /code/requirements.txt