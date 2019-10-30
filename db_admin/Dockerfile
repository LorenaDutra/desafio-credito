FROM python:3.6

ADD db_admin/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app/
WORKDIR /app/
VOLUME /app

# CMD [ "python", "./db_admin.py" ]
CMD [ "/bin/bash" ]
