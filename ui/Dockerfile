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

# Expose gradio port
EXPOSE 7860

# run the ui
CMD python3 ui.py
