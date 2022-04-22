FROM python:3.10.4-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app /app

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]