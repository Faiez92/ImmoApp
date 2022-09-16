FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt