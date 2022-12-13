# select the base image
FROM python:3
# set the environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# set the working directory in the container
COPY . /todo-api
WORKDIR /todo-api
# copy requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy the content of the local src directory to the working directory
COPY . /todo-api