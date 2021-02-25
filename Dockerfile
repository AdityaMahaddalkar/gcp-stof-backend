FROM python:3.9-slim

COPY . /usr/src

WORKDIR /usr/src

RUN pip install -r requirements.txt

ENV PORT 8080

EXPOSE 8080

CMD ["python", "main.py"]