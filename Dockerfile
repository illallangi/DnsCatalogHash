FROM python:3.8.3
LABEL maintainer="Andrew Cole <andrew.cole@illallangi.com>"

WORKDIR /usr/src/app

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD . /usr/src/app

RUN pip3 install .

ENTRYPOINT ["/usr/local/bin/dns-catalog-hash"]