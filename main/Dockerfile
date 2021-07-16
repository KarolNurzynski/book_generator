# Use the Python3.7.2 image
FROM tiangolo/uwsgi-nginx:python3.7

# Update packages list
RUN apt-get update -y 
RUN pip install --upgrade pip

# Install requirements.txt and copy the app
WORKDIR /app
COPY . /app 

RUN pip install -r requirements.txt
ENV FLASK_APP=/main/main.py
# run the command to start uWSGI
CMD ["uwsgi", "uwsgi.ini"]