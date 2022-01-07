FROM python:3.8.9-buster

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /opt/app

ENV PYTHONPATH=/opt/app

RUN apt-get update && \
    apt-get -y install --no-install-recommends libpq-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* **

COPY system/entry_point_public_api.sh /opt/bin/
RUN chmod a+x /opt/bin/*.sh
COPY system/gunicorn_conf.py /opt/gunicorn_conf.py

COPY . .

EXPOSE 80