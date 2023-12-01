FROM python:3.11.4-slim-bullseye
LABEL maintainer="Kittawee Kongpan"
LABEL description="Twelve data Scrapy spiders."

WORKDIR /app

RUN set -xe \
    && apt-get update \
    && apt-get install -y tini


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
COPY .env ./

COPY ./scrapyd.conf /etc/scrapyd/
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
EXPOSE 6800

ENTRYPOINT ["tini", "--"]
CMD ["scrapyd", "--pidfile="]
