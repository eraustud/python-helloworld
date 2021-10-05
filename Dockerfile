FROM python:3.8


COPY . /app
RUN pip install -r requirements.txt
WORKDIR /app


# command to run on container start
CMD [ "python", "app.py" ]
