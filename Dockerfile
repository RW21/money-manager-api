FROM python:3.9-slim-buster

RUN pip install flask gspread gunicorn
COPY app /app
WORKDIR app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]