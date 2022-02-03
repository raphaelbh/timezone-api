FROM python:3.9-alpine
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["main.py" ]