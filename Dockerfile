FROM python:3.6
ENV PYTHONUNBUFFERED 1
COPY src/requirements.txt /
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /
COPY init/files-russian/ src/statements
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:5555"]
# CMD [ "python" "]
