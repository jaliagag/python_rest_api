FROM python:3.11.9-alpine3.19

WORKDIR /app
COPY ./app .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run","--host=0.0.0.0"]
