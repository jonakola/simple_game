FROM python:latest

RUN pip install flask

RUN pip install gunicorn

RUN pip install requests

WORKDIR /app

COPY app/ .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "4", "wsgi:app"]