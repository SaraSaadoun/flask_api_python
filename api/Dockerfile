FROM python:3.11-slim

LABEL maintainer="https://github.com/SaraSaadoun"

RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get -y install python3-pip

# install requiremtnts
RUN pip3 install -r requirements.txt

# copy all files of the current directory to the folder /app
COPY . /app
WORKDIR /app

# Expose Flask port
EXPOSE 5000

# run the flask API
CMD python3 api.py
