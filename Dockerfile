FROM python:3.9.7
ENV PYTHONUNBUFFERED=1

WORKDIR /code
ADD requirements /code/requirements
RUN pip install -r requirements/base.txt
ADD . /code

CMD gunicorn config.wsgi --bind 0.0.0.0:8000 --chdir /code/faty
