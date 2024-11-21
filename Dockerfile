# syntax=docker/dockerfile:1.7-labs
FROM python:3.6-buster
ENV PYTHONUNBUFFERED 1

RUN apt update -y && apt install -y gcc musl-dev libmariadb3 libmariadb-dev texlive-lang-cyrillic texlive-latex-extra

# Install python deps
COPY src/requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Prepare statements
COPY --exclude=init_script.py --exclude=init.txt --exclude=tests/* init /init
WORKDIR /init
RUN python3 build_statements.py

# Bring application & import contest setup
WORKDIR /web_app
COPY src src/
COPY serve.cfg .
COPY init/init.txt /init/
RUN python3 /init/init.py >> /web_app/src/map/apps.py && cp -r /init/files-russian /web_app/src/statements

WORKDIR /web_app
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:5555"]
