FROM python:3-alpine

WORKDIR /app

RUN pip install Flask

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080


COPY app.py app.py

EXPOSE 8080

CMD ["flask", "run"]
