FROM python:3.8

RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app


# command to run on container start
CMD [ "python", "app.py" ]
