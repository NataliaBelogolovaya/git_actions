FROM python:latest
RUN mkdir /app
WORKDIR /app
COPY app/ /app/
EXPOSE 5000
CMD [ "python", "test_app.py" ]