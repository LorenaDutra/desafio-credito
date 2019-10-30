FROM python:3.6
EXPOSE 5000

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app/
WORKDIR /app/
VOLUME /app

CMD ["gunicorn", "--bind=0.0.0.0:5000", "api:app"]
