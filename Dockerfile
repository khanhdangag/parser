FROM python:3.7-alpine
COPY ./src /app
CMD [ "python3", "lexer.py" ]
