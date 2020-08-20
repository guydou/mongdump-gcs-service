FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN wget --no-check-certificate -qO - https://www.mongodb.org/static/pgp/server-4.0.asc  | apt-key add -
RUN echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.0 main" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list
RUN apt update
RUN apt install mongodb-org-tools

COPY ./app /app
COPY ./requirments.txt /app/requirments.txt
RUN pip install -r /app/requirments.txt
