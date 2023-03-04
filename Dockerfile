FROM python:3.10-slim

RUN apt update && mkdir /music

WORKDIR /music

COPY ./src ./src

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt

EXPOSE 8010

CMD ["python", "src/manage.py", "runserver", "0:8000"]
