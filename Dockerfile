FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev
COPY src/requirements.txt /
RUN pip install --upgrade pip && pip install -r requirements.txt

ADD src/. /web_app/src
ADD Dockerfile /web_app
ADD serve.cfg /web_app
WORKDIR web_app

ADD init/init_script.py problems.py
RUN cat problems.py >> src/map/apps.py && rm problems.py

COPY init/files-russian/ src/statements

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:5555"]
