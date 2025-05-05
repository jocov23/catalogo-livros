#config of the container web, based in the image of python, it copy the requirements file and upgrade pip 
FROM python:3.11-alpine

#avoid python write cache archives (avoid "garbage")
ENV PYTHONDONTWRITEBYTECODE=1
#make logs appear immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
#copy all the code of the application into the container
COPY ./app /app