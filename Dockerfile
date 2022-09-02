# docker base
FROM python:3.10.6-slim-bullseye

# set the image workdir
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy content from src folder to the image workdir
COPY src/ ./

# add the workdir to the python path
ENV PYTHONPATH "${PYTHONPATH}:/app"