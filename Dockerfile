# pyhon light image
FROM python:3.9.10-alpine

# copy the code
COPY ./application /application
WORKDIR /application

# install dependencies
RUN pip install -r requirements.txt

# Expose is NOT supported by Heroku
# EXPOSE 5000 		

# run the image as a non-root user
RUN adduser -D appuser
USER appuser

# run the app (CMD is required to run on Heroku)
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi