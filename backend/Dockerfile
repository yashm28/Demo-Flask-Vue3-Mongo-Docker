FROM python:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app /app
RUN pip install gunicorn[gevent]
EXPOSE 5001
CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5001 app:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info