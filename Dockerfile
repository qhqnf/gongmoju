FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    apt-get clean

WORKDIR /code/
ADD . /code
RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED=1


RUN python3 manage.py collectstatic
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]