FROM python:3.7-slim

COPY . /user/src/app
WORKDIR /user/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD python scraper.py