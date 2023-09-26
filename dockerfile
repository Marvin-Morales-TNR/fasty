# Use the official Python image as the base image
FROM python:3.10-alpine
WORKDIR /app
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile
COPY . /app/
EXPOSE 9000

CMD ["pipenv", "run", "server"]
